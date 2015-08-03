import pandas


github_repos_with_kw_docker =

df_github_repos_with_kw_docker_2011_to_2014 = pandas.read_csv(
    'repos_with_docker_2011_to_2014.csv'
)['repository_url']


df_repos_2015 = pandas.read_csv('repos_with_docker_2015.csv')['repo_url']
df_github_repos_with_kw_docker_2015 = map(apiurl_to_repourl, df_repos_2015)


def apiurl_to_repourl(apiurl):
    repo_url = apiurl.replace('api.', '').replace('repos/', '')


df_repo_urls_with_kw_docker_2011_to_2015 = \
    df_github_repos_with_kw_docker_2011_to_2014.append(
        df_github_repos_with_kw_docker_2015
    )
