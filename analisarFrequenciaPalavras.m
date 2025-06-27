function trabalho_pratico_gabriela()
###########################################################################
#
# TRABALHO PRÁTICO - Fundamentos de Tecnologia
# Aluna: Gabriela Cristina Schmitt
# Professor(a): Ana Paula e Débora
#
###########################################################################

# Limpeza do ambiente de trabalho.
clear;
close all;
clc;

fprintf('Iniciando a análise de frequência de palavras-chave...\n');

# 1. Definição dos Parâmetros de Entrada
textos_para_analise = {
    'O uso de inteligência artificial na análise de dados tem crescido exponencialmente. Modelos de machine learning são aplicados para predição e classificação de dados, gerando valor para o negócio. A ética em inteligência artificial é um debate crucial.', ...
    'Este trabalho explora a aplicação de energias renováveis, com foco em energia solar. A eficiência dos painéis solares e o armazenamento de energia são desafios. A sustentabilidade e o impacto ambiental da energia solar foram analisados.', ...
    'A análise de dados em larga escala, ou Big Data, requer novas tecnologias. A computação em nuvem oferece a infraestrutura necessária para o processamento desses dados. A segurança dos dados na nuvem é uma preocupação central para as empresas.', ...
    'Avanços em machine learning, especificamente em redes neurais profundas, revolucionaram a visão computacional. O treinamento de modelos de machine learning exige grande volume de dados e poder computacional. A aplicação em carros autônomos é um exemplo.'
};

# Número de palavras mais frequentes que queremos exibir no gráfico.
top_n_palavras = 15;

# Lista de stopwords em português para serem removidas na contagem.
stopwords_pt = {'a', 'o', 'as', 'os', 'e', 'ou', 'de', 'do', 'da', 'dos', 'das', 'em', 'no', 'na', 'nos', 'nas', 'um', 'uma', 'uns', 'umas', 'com', 'por', 'para', 'pelo', 'pela', 'este', 'esta', 'isto', 'que', 'se', 'sao', 'são', 'foi', 'foram', 'ser', 'tem', 'têm'};

# 2. Chamada da Função de Análise Local
[resultados] = analisarFrequenciaPalavras(textos_para_analise, top_n_palavras, stopwords_pt);

# 3. Exibição dos Resultados no Console
fprintf('\n### RELATÓRIO DA ANÁLISE DE FREQUÊNCIA ###\n');
fprintf('A análise foi concluída. O gráfico com as top %d palavras foi gerado.\n', top_n_palavras);
fprintf('As palavras mais frequentes encontradas foram:\n');

# Garante que não vamos tentar exibir mais palavras do que as que existem.
num_top_display = min(top_n_palavras, numel(resultados.Palavra));

# Loop para exibir os resultados
for i = 1:num_top_display
    fprintf('  %2dº: "%s" - %d ocorrências\n', i, resultados.Palavra{i}, resultados.Frequencia(i));
end

end


function [resultados_analise] = analisarFrequenciaPalavras(textos, numPalavrasPlot, stopwords)
# ----------------------------------------------------------------------------------
# ENTRADAS (Inputs):
#   - textos: (cell array) Array de células onde cada célula contém uma string de texto.
#   - numPalavrasPlot: (integer) Número de palavras a serem exibidas no gráfico.
#   - stopwords: (cell array) Lista de palavras a serem ignoradas na análise.
#
# SAÍDA (Output):
#   - resultados_analise: (struct) Estrutura contendo os campos .Palavra e .Frequencia
# ----------------------------------------------------------------------------------

    # ETAPA 1: Pré-processamento dos Textos
    textoCompleto = strjoin(textos, ' ');                                  # strjoin: Unifica todos os textos em uma única string.
    textoCompleto = lower(textoCompleto);                                  # lower: Converte para minúsculas para uniformizar.
    textoCompleto = regexprep(textoCompleto, '[.,;:"''()\[\]?!]', '');      # regexprep: Remove pontuações.
    todasPalavras = strsplit(textoCompleto, ' ');                          # strsplit: Divide o texto em um array de palavras.

    # ETAPA 2: Remoção de Stopwords
    indicesManter = ~ismember(todasPalavras, stopwords);                   # ismember: Identifica palavras que NÃO são stopwords.
    todasPalavras = todasPalavras(indicesManter);                          # Indexação Lógica: Mantém apenas as palavras válidas.
    todasPalavras = todasPalavras(~strcmp(todasPalavras, ''));             # strcmp: Remove células vazias.

    # ETAPA 3: Contagem da Frequência
    palavrasUnicas = unique(todasPalavras);                                # unique: Cria uma lista de palavras sem repetição.
    frequencias = zeros(numel(palavrasUnicas), 1);                         # zeros: Inicializa o vetor de contagem.

    # for: Laço de repetição para contar a frequência de cada palavra.
    for i = 1:numel(palavrasUnicas)
        frequencias(i) = sum(strcmp(palavrasUnicas{i}, todasPalavras));    # sum/strcmp: Soma as ocorrências de cada palavra.
    end

    # ETAPA 4: Organização dos Resultados
    [frequenciasOrdenadas, idx] = sort(frequencias, 'descend');            # sort: Ordena as frequências do maior para o menor.
    palavrasOrdenadas = palavrasUnicas(idx);                               # Reordena as palavras para corresponder à ordem.

    # Atribuição da Saída como uma estrutura (struct).
    resultados_analise.Palavra = palavrasOrdenadas;
    resultados_analise.Frequencia = frequenciasOrdenadas;

    # ETAPA 5: Geração do Gráfico
    # if: Garante que não tentaremos plotar mais palavras do que as que existem.
    if numPalavrasPlot > numel(palavrasOrdenadas)
        numPalavrasPlot = numel(palavrasOrdenadas);
    end

    palavrasPlot = resultados_analise.Palavra(1:numPalavrasPlot);
    frequenciasPlot = resultados_analise.Frequencia(1:numPalavrasPlot);

    figure;                                                                # figure: Cria uma nova janela para a figura.

    # barh: Cria o gráfico de barras horizontais.
    # flip é usado para que a palavra mais frequente apareça no topo.
    # 'm' define a cor magenta == rosa
    barh(flip(frequenciasPlot), 'm');

    yticks(1:numPalavrasPlot);                                             # yticks: Define as posições dos marcadores no eixo Y.
    yticklabels(flip(palavrasPlot));                                       # yticklabels: Define os rótulos do eixo Y como as palavras.

    title(['Top ', num2str(numPalavrasPlot), ' Palavras Mais Frequentes']); # title: Define o título do gráfico.
    xlabel('Frequência de Ocorrência');                                    # xlabel: Define o rótulo do eixo X.
    ylabel('Palavras-Chave');                                              # ylabel: Define o rótulo do eixo Y.

    grid on;                                                               # grid: Ativa a grade de fundo.
    ylim([0.5, numPalavrasPlot + 0.5]);                                    # ylim: Ajusta o espaçamento do eixo Y.
    set(gca, 'FontSize', 10);                                              # set: Ajusta o tamanho da fonte para melhor leitura.

end
