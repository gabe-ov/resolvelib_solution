REPOSITORY = {
    # Habilidades Comuns (usadas por várias classes)
    ("habilidade", "golpe_basico"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("habilidade", "defesa"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("habilidade", "corrida"): {
        "1.0.0": [],
        "1.1.0": [],
    },

    # Classes
    ("classe", "mago_arcano"): {
        "1.0.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "corrida", "version_spec": ">=1.0"},
        ],
        "1.0.1": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "corrida", "version_spec": ">=1.0"},
        ],
        "1.1.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.1"},
            {"type": "habilidade", "slug": "corrida", "version_spec": ">=1.1"},
        ],
        "1.1.1": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.1"},
            {"type": "habilidade", "slug": "corrida", "version_spec": ">=1.1"},
        ],
    },
    ("classe", "guerreiro_berserker"): {
        "1.0.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "defesa", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "furia", "version_spec": ">=1.0,<2.0"},
            {"type": "equipamento", "slug": "espada_lendaria", "version_spec": ">=1.0"},
        ],
        "1.0.1": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "defesa", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "furia", "version_spec": ">=1.0,<2.0"},
            {"type": "equipamento", "slug": "espada_lendaria", "version_spec": ">=1.0"},
        ],
        "1.1.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "defesa", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "furia", "version_spec": ">=1.0,<2.0"},
            {"type": "equipamento", "slug": "espada_lendaria", "version_spec": ">=1.0"},
        ],
        "2.0.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.1"},
            {"type": "habilidade", "slug": "defesa", "version_spec": ">=1.1"},
            {"type": "habilidade", "slug": "furia_avancada", "version_spec": "==2.0"},
            {"type": "equipamento", "slug": "espada_lendaria", "version_spec": ">=2.0"},
        ],
    },
    ("classe", "arqueiro_atirador"): {
        "1.0.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "corrida", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "tiro_certeiro", "version_spec": ">=1.0"},
            {"type": "equipamento", "slug": "arco_longo", "version_spec": ">=1.0"},
        ],
        "1.1.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.1"},
            {"type": "habilidade", "slug": "corrida", "version_spec": ">=1.1"},
            {"type": "habilidade", "slug": "tiro_certeiro", "version_spec": ">=1.0"},
            {"type": "equipamento", "slug": "arco_longo", "version_spec": ">=1.0"},
        ],
    },
    ("classe", "paladino"): {
        "1.0.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "defesa", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "proteção_divina", "version_spec": ">=1.0"},
            {"type": "equipamento", "slug": "armadura_sagrada", "version_spec": ">=1.0"},
            {"type": "equipamento", "slug": "espada_lendaria", "version_spec": ">=1.0"},
            {"type": "magia", "slug": "cura_maior", "version_spec": ">=1.0"},
        ],
        "1.1.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.1"},
            {"type": "habilidade", "slug": "defesa", "version_spec": ">=1.1"},
            {"type": "habilidade", "slug": "proteção_divina", "version_spec": ">=1.1"},
            {"type": "equipamento", "slug": "armadura_sagrada", "version_spec": ">=1.0"},
            {"type": "equipamento", "slug": "espada_lendaria", "version_spec": ">=1.0"},
            {"type": "magia", "slug": "cura_maior", "version_spec": ">=1.1"},
        ],
    },
    ("classe", "necromante"): {
        "1.0.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.0"},
            {"type": "habilidade", "slug": "controle_mortis", "version_spec": ">=1.0"},
            {"type": "magia", "slug": "maldição_sombrio", "version_spec": ">=0.8"},
            {"type": "equipamento", "slug": "cajado_das_almas", "version_spec": ">=1.0"},
        ],
        "1.2.0": [
            {"type": "habilidade", "slug": "golpe_basico", "version_spec": ">=1.1"},
            {"type": "habilidade", "slug": "controle_mortis", "version_spec": ">=1.1"},
            {"type": "magia", "slug": "maldição_sombrio", "version_spec": ">=1.0"},
            {"type": "magia", "slug": "raio_letal", "version_spec": ">=1.0"},
            {"type": "equipamento", "slug": "cajado_das_almas", "version_spec": ">=1.1"},
        ],
    },

    # Habilidades (comuns e específicas)
    ("habilidade", "golpe_basico"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("habilidade", "defesa"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("habilidade", "corrida"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("habilidade", "bola_de_fogo"): {
        "1.0.0": [
            {"type": "magia", "slug": "fogo_basico", "version_spec": ">=1.0"},
        ],
        "1.1.0": [
            {"type": "magia", "slug": "fogo_basico", "version_spec": ">=1.0"},
        ],
    },
    ("habilidade", "escudo_de_gelo"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("habilidade", "furia"): {
        "1.0.0": [],
        "1.0.1": [],
        "1.1.0": [],
    },
    ("habilidade", "furia_avancada"): {
        "2.0.0": [
            {"type": "habilidade", "slug": "furia", "version_spec": ">=1.1.0"},
        ],
    },
    ("habilidade", "tiro_certeiro"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("habilidade", "proteção_divina"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("habilidade", "controle_mortis"): {
        "1.0.0": [],
        "1.1.0": [],
    },

    # Equipamentos
    ("equipamento", "cajado_arcano"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("equipamento", "espada_lendaria"): {
        "1.0.0": [],
        "2.0.0": [],
    },
    ("equipamento", "arco_longo"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("equipamento", "armadura_sagrada"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("equipamento", "cajado_das_almas"): {
        "1.0.0": [],
        "1.1.0": [],
    },

    # Magias
    ("magia", "cura_maior"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("magia", "maldição_sombrio"): {
        "0.8.0": [],
        "1.0.0": [],
    },
    ("magia", "fogo_basico"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("magia", "raio_letal"): {
        "1.0.0": [],
        "1.1.0": [],
    },

    # Inimigos
    ("inimigo", "goblin"): {
        "1.0.0": [],
        "1.1.0": [],
    },
    ("inimigo", "dragao_fogo"): {
        "3.0.0": [
            {"type": "magia", "slug": "bola_de_fogo", "version_spec": ">=1.0"},
        ],
    },

    # Mapas
    ("mapa", "floresta_encantada"): {
        "1.0.0": [
            {"type": "inimigo", "slug": "goblin", "version_spec": ">=1.0"},
        ],
        "1.1.0": [
            {"type": "inimigo", "slug": "goblin", "version_spec": ">=1.1"},
        ],
    },
    ("mapa", "montanhas_fumegantes"): {
        "1.0.0": [
            {"type": "inimigo", "slug": "dragao_fogo", "version_spec": ">=3.0"},
        ],
    },
}
