from rest_framework import serializers

from shop.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    email = serializers.CharField(read_only=True)
    # email = serializers.EmailField()

    # def create(self, validated_data):
    #     created new instance
    #     return instance
    #
    # def update(self, instance, validated_data):
    #     return instance

    class Meta:
        model = Author
        fields = ('id', 'name', 'email',)

    def validate_name(self, value):
        if ['/', '%'] in value:
            raise serializers.ValidationError('invalid char in name field')
        return value

    def validate(self, attrs):
        # check object level validation,
        # if any raise serializer.ValidationError
        return attrs


class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Book
        fields = ('id', 'name', 'price', 'is_published', 'author_id',)

