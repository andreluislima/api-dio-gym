from workout_api.atleta.atleta_model import AtletaModel
from workout_api.categoria.categoria_model import CategoriaModel
from workout_api.centro_treinamento.centro_treinamento_model import CentroTreinamentoModel

def init_relationships():
    CategoriaModel.atletas.property.mapper
    CentroTreinamentoModel.atletas.property.mapper
    AtletaModel.categoria.property.mapper
    AtletaModel.centro_treinamento.property.mapper
