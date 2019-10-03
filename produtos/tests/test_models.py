from mixer.backend.django import mixer

import pytest
from django.test import TestCase

@pytest.mark.django_db

class TestModels:
    
    def test_produto_em_esqtoque(self):
        produto = mixer.blend(
            'produtos.Produto',
            quantidade=1
        )

        assert produto.tem_no_estoque == True
    