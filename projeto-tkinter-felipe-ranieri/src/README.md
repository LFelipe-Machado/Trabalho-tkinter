# Trabalho-tkinter

## Nome da Equipe
Felipe e Ranieri

## Integrantes
- Felipe Machado (LFelipe-Machado)
- Ranieri Pereira (RanieriFilho)

## Descrição do Sistema
Sistema de desenho vetorial desenvolvido em Python com Tkinter, no estilo Google Drawings e LibreOffice Draw. Permite criar, editar e salvar desenhos contendo formas geométricas como retângulos, ovais, círculos, linhas, rabiscos e polígonos, com suporte a cores de borda e preenchimento.

O sistema foi desenvolvido seguindo o padrão de arquitetura MVC (Model-View-Controller), com as classes separadas em módulos distintos.

## Estrutura do Projeto
```
Trabalho-tkinter/
├── src/
│   └── trabalho_tkinter/
│       ├── main.py              # Ponto de entrada da aplicação
│       ├── modelo/
│       │   └── figuras.py       # Classes do modelo (Figura e subclasses, Desenho)
│       ├── visao/
│       │   └── visao.py         # Classe da visão (interface gráfica)
│       └── controlador/
│           └── controlador.py   # Classe do controlador (eventos e lógica)
├── docs/                        # Documentação HTML gerada pelo Pydoc
└── README.md
```

## Classes Documentadas
- `Figura` — classe base abstrata
- `FiguraDeArrastar` — classe intermediária para figuras de arrastar
- `Linha`
- `Retangulo`
- `Oval`
- `Circulo`
- `Rabisco`
- `Poligono`
- `Desenho`
- `Visao`
- `Controlador`

**Total: 11 classes documentadas**

## Métodos Documentados
| Classe | Métodos |
|---|---|
| Figura | `__init__`, `desenhar`, `incompleta`, `to_dict` |
| FiguraDeArrastar | `__init__`, `atualizar`, `incompleta`, `to_dict` |
| Linha | `__init__`, `desenhar` |
| Retangulo | `desenhar` |
| Oval | `desenhar` |
| Circulo | `atualizar`, `desenhar` |
| Rabisco | `__init__`, `adicionar_ponto`, `desenhar`, `incompleta`, `to_dict` |
| Poligono | `__init__`, `adicionar_ponto`, `desenhar`, `incompleta`, `to_dict` |
| Desenho | `__init__`, `salvar`, `abrir` |
| Visao | `__init__`, `_criar_menu`, `_criar_widgets`, `escolher_cor_borda`, `escolher_cor_preenchimento`, `pedir_caminho_salvar`, `pedir_caminho_abrir`, `desenhar_figuras`, `desenhar_figuranova` |
| Controlador | `__init__`, `iniciar_figuranova`, `atualizar_figuranova`, `incluir_figuranova`, `finalizar_poligono`, `salvar`, `abrir` |

**Total: 36 métodos documentados**

## Como Visualizar a Documentação
1. Navegue até a pasta do projeto no terminal
2. Execute os comandos abaixo para gerar os HTMLs:
```bash
python -m pydoc -w modelo.figuras
python -m pydoc -w visao.visao
python -m pydoc -w controlador.controlador
python -m pydoc -w main
```
3. Mova os arquivos `.html` gerados para a pasta `docs/`
4. Abra os arquivos `.html` no navegador
