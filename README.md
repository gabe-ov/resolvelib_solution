# RPG Dependency Resolver

Este projeto demonstra o uso da biblioteca **resolvelib** para resolver dependências entre versões de entidades de um universo RPG (classes, habilidades, magias, equipamentos, etc).

---

## Estrutura do Dataset

O dataset define versões e dependências para diversos tipos, como:

* Classes (ex: guerreiro\_berserker, mago\_arcano, paladino)
* Habilidades comuns e específicas
* Magias
* Equipamentos
* Inimigos
* Mapas

Cada item pode ter dependências e restrições de versões para outros itens.

---

## Como rodar

### 1. Criar e ativar ambiente virtual

```bash
uv venv
source .venv/bin/activate
```

### 2. Instalar dependências

```bash
uv add --requirements requirements.txt
```

Certifique-se que o arquivo `requirements.txt` contém pelo menos:

```
resolvelib
```

### 3. Executar a resolução

```bash
python main.py
```

---