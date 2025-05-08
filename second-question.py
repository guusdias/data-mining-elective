import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)

    relevant_columns = [
        'Artist Genres', 'Danceability', 'Energy', 'Valence', 'Acousticness',
        'Instrumentalness'
    ]
    df = df[relevant_columns]

    bins = [0, 0.33, 0.66, 1]
    labels = ['Low', 'Medium', 'High']

    df['Danceability'] = pd.cut(df['Danceability'], bins=bins, labels=labels,
                                include_lowest=True)
    df['Energy'] = pd.cut(df['Energy'], bins=bins, labels=labels,
                          include_lowest=True)
    df['Valence'] = pd.cut(df['Valence'], bins=bins, labels=labels,
                           include_lowest=True)
    df['Acousticness'] = pd.cut(df['Acousticness'], bins=bins, labels=labels,
                                include_lowest=True)
    df['Instrumentalness'] = pd.cut(df['Instrumentalness'], bins=bins,
                                    labels=labels, include_lowest=True)

    df['Artist Genres'] = df['Artist Genres'].str.split(',')
    df = df.explode('Artist Genres')
    df['Artist Genres'] = df['Artist Genres'].str.strip()

    one_hot_df = pd.get_dummies(df, columns=['Artist Genres', 'Danceability',
                                             'Energy', 'Valence',
                                             'Acousticness',
                                             'Instrumentalness'])

    return one_hot_df



def generate_association_rules(one_hot_df, min_support=0.01,
                               min_confidence=0.5):
    frequent_itemsets = apriori(one_hot_df, min_support=min_support,
                                use_colnames=True)

    rules = association_rules(frequent_itemsets, metric="confidence",
                              min_threshold=min_confidence)

    rules = rules[rules['lift'] > 1]

    rules = rules.sort_values(by='confidence', ascending=False)

    return frequent_itemsets, rules


def display_rules(rules):
    print("\nRegras de Associação Geradas:")
    for idx, rule in rules.iterrows():
        antecedents = ', '.join(list(rule['antecedents']))
        consequents = ', '.join(list(rule['consequents']))
        print(f"Regra {idx + 1}: {antecedents} -> {consequents}")
        print(f"Suporte: {rule['support']:.4f}")
        print(f"Confiança: {rule['confidence']:.4f}")
        print(f"Lift: {rule['lift']:.4f}")
        print("-" * 50)


def main():
    file_path = 'dataset_spotify.csv'

    one_hot_df = load_and_preprocess_data(file_path)
    frequent_itemsets, rules = generate_association_rules(one_hot_df,
                                                          min_support=0.01,
                                                          min_confidence=0.5)

    print("Itemsets Frequentes:")
    print(frequent_itemsets[['support', 'itemsets']].to_string(index=False))

    display_rules(rules)

if __name__ == "__main__":
    main()