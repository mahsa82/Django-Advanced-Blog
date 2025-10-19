from rest_framework import serializers
from ...models import Post,Category
from account.models import Profile

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        

class PostSerializer(serializers.ModelSerializer):
    published_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField()
    
    # category = serializers.SlugRelatedField(many=False,slug_field='name',queryset=Category.objects.all())
    # category = CategorySerializer()
    class Meta :
        model = Post
        fields = ['id','author','title','content','snippet','category','status','relative_url','absolute_url','created_date','published_date']
        read_only_fields = ['author']
    
    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
        
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id','name']
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        rep['state'] = 'list'
        if request.parser_context.get('kwargs').get('pk'):
            rep['state'] = 'single'
            rep.pop('snippet',None)
            rep.pop('relative_url',None)
            rep.pop('absolute_url',None)
        else:
            rep.pop('content',None)
        rep['category'] = CategorySerializer(instance.category,context={'request':request}).data 
        
        return rep
    
    def create(self,validate_date):
        validate_date['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validate_date)