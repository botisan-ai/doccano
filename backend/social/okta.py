from django.conf import settings
from django.http import HttpResponseRedirect
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.okta.views import OktaOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView


class OktaLogin(SocialLoginView):
    adapter_class = OktaOAuth2Adapter
    callback_url = settings.SOCIALACCOUNT_PROVIDERS.get("okta").get("OKTA_CALLBACK_URL")
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)

        self.login()
        return HttpResponseRedirect(settings.SOCIALACCOUNT_PROVIDERS.get("okta").get("OKTA_CALLBACK_URL").replace('/social/complete/okta-oauth2/', '/projects'))