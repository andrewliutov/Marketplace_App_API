from rest_framework import serializers
from shop.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    """Сериализатор для магазина"""
    class Meta:
        model = Shop
        fields = ('id', 'name', 'state',)

    def update(self, insatace, validated_data):
        user_shop = self.context['request'].user.shop_to_user
        if user_shop.id == self.data['id']:
            state = validated_data.get('state')
            validated_data.update(
                {
                    'state': state
                }
            )
            return super().create(validated_data)
        else:
            raise serializers.ValidationError(
                'Вы не являетесь администратором этого магазина')