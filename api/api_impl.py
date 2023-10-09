import concurrent.futures

from flask import request, jsonify

from service import web_scraper, api_search_engine
from service import simple_similar as similar
from utils.logger import logger


def scrape_and_store(site):
    data, err = web_scraper.scrape_site(site, False)
    if err:
        return {"error": str(err)}
    return data


def search():
    try:
        query = request.get_json()
        logger.info("query=%s", query)
        if not query:
            return jsonify({"error": "Invalid JSON input"}), 400

        print(f"post query: {query}")

        if query.get("query").startswith("http"):
            # 直接抓取网站
            data, err = web_scraper.scrape_site(query.get("query"), False)
            if err:
                return jsonify({"error": str(err)}), 500
            return jsonify({"data": data, "message": "Success"}), 200

        # 获取热门网站
        top_sites, err = api_search_engine.fetch_top_sites_from_api(query.get("query"))
        if err:
            return jsonify({"error": str(err)}), 500
        # 抓取网站
        scraped_data = []
        # 使用 ThreadPoolExecutor 实现并发
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = list(executor.map(scrape_and_store, top_sites))

        for result in results:
            if "error" in result:
                return jsonify({"error": result["error"]}), 500
            scraped_data.append(result)

        matched_data, err = similar.perform_vector_matching(query.get("query"), scraped_data)
        if err:
            return jsonify({"error": str(err)}), 500

        return jsonify({"data": matched_data, "message": "Success"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def match_data():
    try:
        req = request.get_json()
        # {"scraped_data":[], "query": ""}
        logger.info("req=%s", req)
        matched_data, err = similar.perform_vector_matching(req.get("query"), req.get("scraped_data"))
        if err:
            return jsonify({"error": str(err)}), 500
        return jsonify({"data": matched_data, "message": "Success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def hello():
    return jsonify({"hello": "world"}),200