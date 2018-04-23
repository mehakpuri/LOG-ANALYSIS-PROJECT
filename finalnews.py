#!/usr/bin/env python3
# project 3- log analysis.
import psycopg2

# Database queries
# 1. What are the three most popular articles of all time?
query_1 = """SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
    """

# 2. Who are the most popular article authors of all time?
query_2 = """select authors.name, count(*) as num
            from articles, authors, log
            where log.status='200 OK'
            and authors.id = articles.author
            and articles.slug = substr(log.path, 10)
            group by authors.name
            order by num desc;
            """

# 3. On which day did more than 1% of requests lead to errors?
query_3 = """
SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
    """


# Query data from the database and returning the result
def query_database(quer):
    db = psycopg2.connect(database="news")
    cursor = db.cursor()
    cursor.execute(quer)
    result = cursor.fetchall()
    db.close()
    return result


# Printing the title
def get_title(article_title):
    print ("\n" + article_title + "\n")


# Printing the top three articles of all time
def get_toparticles():
    get_toparticles = query_database(query_1)
    get_title("1) TOP 3 ARTICLES OF ALL TIME")

    for article_title, num in get_toparticles:
        print(" \"{}\" -- {} views".format(article_title, num))


# Printing the top authors of all time
def get_topauthors():
    get_topauthors = query_database(query_2)
    get_title("2) TOP AUTHORS OF ALL TIME")

    for name, num in get_topauthors:
        print(" {} -- {} views".format(name, num))


# Print the days in which there were more than 1% bad requests
def high_error():
    high_error = query_database(query_3)
    get_title("3) DAYS WITH MORE THAN ONE PERCENTAGE OF BAD REQUESTS")

    for i in high_error:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print(date + " -- " + errors)

# calling result functions for the output
get_toparticles()
get_topauthors()
high_error()
