import re

import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def contains_chinese(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    return bool(pattern.search(text))


def perform_vector_matching(query, scraped_data):
    # 分词查询文本
    query_tokens = list(jieba.cut(query))



    # 分词文本数据
    tokenized_data = [" ".join(jieba.cut(text)) for text in scraped_data]

    # 创建TF-IDF向量化器
    tfidf_vectorizer = TfidfVectorizer()

    # 计算TF-IDF矩阵
    tfidf_matrix = tfidf_vectorizer.fit_transform(tokenized_data)

    # 计算查询文本的TF-IDF向量
    query_vector = tfidf_vectorizer.transform([" ".join(query_tokens)])

    # 计算余弦相似度
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix)
    results = cosine_similarities[0]
    # 创建一个包含索引和相似度得分的元组列表
    indexed_results = [(i, cosine_score) for i, cosine_score in enumerate(results)]

    # 根据相似度得分对结果进行排序（降序）
    sorted_results = sorted(indexed_results, key=lambda x: x[1], reverse=True)

    # 获取匹配度最高的文本
    top_match_index, top_match_score = sorted_results[0]
    top_match_text = scraped_data[top_match_index]

    # 打印相似度结果
    for i, cosine_score in sorted_results:
        print(f"文本{i + 1}与查询文本的余弦相似度：{cosine_score}")

    # 返回匹配度最高的文本
    return top_match_text, None