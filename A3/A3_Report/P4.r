TFIDF_rank <- c(1,2,3,4,5,5,7,8,8,10)
page_rank <- c(1,6,6,10,1,6,1,1,1,9)
alexa_rank <- c(3,8,7,10,4,5,2,1,6,9)

pearson_TFIDF_PR <- cor(TFIDF_rank, page_rank)
pearson_TFIDF_PR 
kendallTauB_TFIDF_PR <- cor(TFIDF_rank, page_rank, method="kendall")
kendallTauB_TFIDF_PR


pearson_TFIDF_alexa <- cor(TFIDF_rank, alexa_rank)
pearson_TFIDF_alexa 
kendallTauB_TFIDF_alexa <- cor(TFIDF_rank, alexa_rank, method="kendall")
kendallTauB_TFIDF_alexa


pearson_PR_alexa <- cor(page_rank, alexa_rank)
pearson_PR_alexa 
kendallTauB_PR_alexa <- cor(page_rank, alexa_rank, method="kendall")
kendallTauB_PR_alexa