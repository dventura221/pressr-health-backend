from rest_framework import serializers
from .models import User, Provider, Reading, Comment


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        many=True,
        read_only=True
    )

    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )

    provider_url = serializers.ModelSerializer.serializer_url_field(
        view_name='provider_detail'
    )

    class Meta:
        model = Provider
        fields = (
            'id', 'provider_url', 'first_name', 'last_name', 'photo_url', 'provider_type', 'users',
            'comments',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    readings = serializers.HyperlinkedRelatedField(
        view_name='reading_detail',
        many=True,
        read_only=True
    )

    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )

    provider = serializers.HyperlinkedRelatedField(
        view_name='provider_detail',
        read_only=True
    )

    provider_id = serializers.PrimaryKeyRelatedField(
        queryset=Provider.objects.all(),
        source='provider'
    )

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'dob', 'photo_url', 'provider', 'provider_id', 'readings',
            'comments',
        )


class ReadingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    class Meta:
        model = Reading
        fields = (
            'id', 'user', 'user_id', 'systolic', 'diastolic', 'created_at', 'updated_at',
        )


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    provider = serializers.HyperlinkedRelatedField(
        view_name='provider_detail',
        read_only=True
    )

    provider_id = serializers.PrimaryKeyRelatedField(
        queryset=Provider.objects.all(),
        source='provider'
    )

    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user'
    )

    reading = serializers.HyperlinkedRelatedField(
        view_name='reading_detail',
        read_only=True
    )

    reading_id = serializers.PrimaryKeyRelatedField(
        queryset=Reading.objects.all(),
        source='reading'
    )

    class Meta:
        model = Comment
        fields = (
            'id', 'provider', 'provider_id', 'user', 'user_id', 'reading', 'reading_id', 'author_of_comment', 'content', 'created_at', 'updated_at',
        )
