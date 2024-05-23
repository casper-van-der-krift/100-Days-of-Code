# Ik heb al je imports in 1 file gezet, maakt het ook overzichtelijker
from src.config import *
# Ik heb je email functies in een andere file gezet, maakt het wat overzichtelijker
from src.utils import write_email, send_email


def get_birthdays(df: pd.DataFrame):
    # 2. Filter dataframe on birthdays matching today
    now = dt.datetime.now()
    today = now.day
    this_month = now.month

    current_month_day_filter = (df.month == this_month) & (df.day == today)
    df_filtered = df[current_month_day_filter]
    
    # Onderstaande lines zijn niet nodig. 
    # Als je die 'empty' variable zo gebruikt is je code iets minder goed te lezen dan wanneer je gewoon zegt 'if not df.empty:'
    # empty = df_filtered.empty

    # Al hoewel het niet slecht is, hoeft onderstaande ook niet perse, je kunt namelijk ook over rijen van een dataframe loopen
    # birthday_dict_list = df_filtered.to_dict(orient='records')
    return df_filtered


if __name__ == "__main__":
    # ik zou altijd een if __name__ statement in je script zetten, dat maakt de "flow" net wat overzichtelijker
    # vervolgens is het onderstaande een stylistische keuze, want je kunt data laden op 100 verschillende manieren. 
    df = pd.read_csv(
        join(DATA_FOLDER, BIRTHDAY_FILE)
    )

    # zet individuele onderdelen in een functie
    bd_df = get_birthdays(df)

    if not bd_df.empty:
        send_emails(bd_df)




















