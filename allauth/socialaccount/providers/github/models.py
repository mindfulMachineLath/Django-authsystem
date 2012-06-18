from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.models import OAuth2Provider


class GitHubAccount(ProviderAccount):
    pass

class GitHubProvider(OAuth2Provider):
    id = 'github'
    name = 'GitHub'
    package = 'allauth.socialaccount.providers.github'
    account_class = GitHubAccount

providers.registry.register(GitHubProvider)
