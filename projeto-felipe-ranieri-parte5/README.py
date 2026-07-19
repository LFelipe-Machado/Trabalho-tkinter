# Trabalho-tkinter

## Nome da Equipe
Felipe e Ranieri

## Integrantes
- Felipe Machado (LFelipe-Machado)
- Ranieri Pereira (RanieriFilho)

## Descrição do Sistema
Sistema de desenho vetorial desenvolvido em Python com Tkinter, no estilo Google Drawings e LibreOffice Draw. Permite criar, editar e salvar desenhos contendo formas geométricas como retângulos, ovais, círculos, linhas, rabiscos e polígonos, com suporte a cores de borda e preenchimento.

O sistema foi desenvolvido seguindo o padrão de arquitetura MVC (Model-View-Controller), com as classes separadas em módulos distintos. A partir da Etapa 5, o Controlador também aplica o padrão de projeto **State** para escolher o comportamento de cada ferramenta de desenho.

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
│           ├── controlador.py   # Classe do controlador (eventos e coordenação)
│           └── estados.py       # Estados de desenho (padrão State)
├── docs/                        # Documentação HTML gerada pelo Pydoc
└── README.md
```

## Padrão State (Etapa 5)
Antes desta etapa, o `Controlador` decidia o que fazer em cada evento de mouse consultando o tipo de figura selecionado (`tipofigura_var`) através de uma cadeia de `if`/`elif` repetida em `iniciar_figuranova`, `atualizar_figuranova` e `incluir_figuranova`. Sempre que uma ferramenta nova fosse adicionada, seria preciso lembrar de tocar nos três métodos.

Essa lógica foi extraída para `controlador/estados.py`, onde cada ferramenta (Linha, Retângulo, Oval, Círculo, Rabisco e Polígono) virou uma classe de estado que sabe reagir sozinha aos eventos de mouse:

- **`EstadoDesenho`** — interface abstrata com `iniciar`, `atualizar`, `incluir` e `finalizar_poligono` (este último já com uma implementação padrão comum a todos os estados).
- **`EstadoFiguraDeArrastar`** — estado-base para as quatro figuras definidas por dois pontos (Linha, Retângulo, Oval, Círculo), que compartilham o mesmo comportamento de iniciar/atualizar/incluir; cada subclasse só define qual figura criar.
- **`EstadoRabisco`** e **`EstadoPoligono`** — estados com comportamento próprio (acúmulo de pontos e finalização por clique direito, respectivamente).

O `Controlador` agora mantém um dicionário `{tipo: estado}` e apenas delega o evento ao estado correspondente à seleção atual da Visão — nenhum de seus métodos de evento precisa mais perguntar "qual figura é essa?".

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
- `EstadoDesenho` — interface abstrata dos estados (padrão State)
- `EstadoFiguraDeArrastar` — estado-base para as figuras de arrastar
- `EstadoLinha`
- `EstadoRetangulo`
- `EstadoOval`
- `EstadoCirculo`
- `EstadoRabisco`
- `EstadoPoligono`

**Total: 19 classes documentadas**

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
| Controlador | `__init__`, `_estado_atual`, `iniciar_figuranova`, `atualizar_figuranova`, `incluir_figuranova`, `finalizar_poligono`, `salvar`, `abrir` |
| EstadoDesenho | `iniciar`, `atualizar`, `incluir`, `finalizar_poligono` |
| EstadoFiguraDeArrastar | `_criar_figura`, `iniciar`, `atualizar`, `incluir` |
| EstadoLinha | `_criar_figura` |
| EstadoRetangulo | `_criar_figura` |
| EstadoOval | `_criar_figura` |
| EstadoCirculo | `_criar_figura` |
| EstadoRabisco | `iniciar`, `atualizar`, `incluir` |
| EstadoPoligono | `iniciar`, `atualizar`, `incluir` |

**Total: 62 métodos documentados**

## Como Visualizar a Documentação
1. Navegue até a pasta `src/trabalho_tkinter` no terminal
2. Execute os comandos abaixo para gerar os HTMLs:
```bash
python -m pydoc -w modelo.figuras
python -m pydoc -w visao.visao
python -m pydoc -w controlador.estados
python -m pydoc -w controlador.controlador
python -m pydoc -w main
```
   > O comando `-w main` abre uma janela do Tkinter (é o ponto de entrada da aplicação); feche a janela para o pydoc concluir a geração do HTML.
3. Mova os arquivos `.html` gerados para a pasta `docs/`
4. Abra os arquivos `.html` no navegador
