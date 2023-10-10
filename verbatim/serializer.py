from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        data = {}
        token = super().get_token(user)

        data["refresh"] = str(token)
        data["access"] = str(token.access_token)

        return data