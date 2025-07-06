import streamlit as st
import random

mood_options = {
    "Happy": {
        "songs": [
            ("Shayad – Love Aaj Kal", "https://open.spotify.com/track/2gYnu5DYCi7jFo3S1cWlZ0"),
            ("Gal Mitthi Mitthi – Aisha", "https://open.spotify.com/track/3DuTdWdzWQW0PxsTYdKZvg"),
            ("Maate Vinaduga – Taxiwaala", "https://open.spotify.com/track/2KxCddJ1S1sJdUhoUO3Ycd"),
            ("Kanulanu Thaake – Manam", "https://open.spotify.com/track/0Ruh8R3k0STKrbjHlnWavH"),
            ("Butter – BTS", "https://open.spotify.com/track/3VqeTFIvhxu3DIe4eZ5ID5"),
            ("Blue Hour – TXT", "https://open.spotify.com/track/3e8vFv0v1w0FHeUgZ0iRrb")
        ],
        "quotes": [
            "Happiness is not something ready-made. It comes from your own actions. – Dalai Lama",
            "The purpose of our lives is to be happy. – Dalai Lama"
        ],
        "gif": "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif"
    },

    "Sad": {
        "songs": [
            ("Agar Tum Saath Ho – Tamasha", "https://open.spotify.com/track/3GZoW2U6kQpB3lYptKQ9lP"),
            ("Channa Mereya – Ae Dil Hai Mushkil", "https://open.spotify.com/track/5iZx4zFZ87u2yF2YkLhYjC"),
            ("Oohale – Jaanu", "https://open.spotify.com/track/5GFHd6y08AKyMe2s9qZDR2"),
            ("Nuvvunte Naa Jathagaa – Iddarammayilatho", "https://open.spotify.com/track/4E4uwzThVZqfAOJAKdHqEf"),
            ("The Truth Untold – BTS", "https://open.spotify.com/track/0vQG6VxXGjdKfjvVLU1TUE"),
            ("20cm – TXT", "https://open.spotify.com/track/2Bjy7Y7OD6Uj4NnssJmVdT")
        ],
        "quotes": [
            "Tears come from the heart and not from the brain. – Leonardo da Vinci",
            "Every human walks around with a certain kind of sadness. – Brad Pitt"
        ],
        "gif": "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif"
    },

    "Stressed": {
        "songs": [
            ("Phir Le Aaya Dil – Barfi", "https://open.spotify.com/track/5PpkrXnT64DZ0YxWvHcjq9"),
            ("Dil Diyan Gallan – Tiger Zinda Hai", "https://open.spotify.com/track/2F8CPmSQ80FEwQzO1W6QzX"),
            ("The Life of Ram – 96 (Telugu)", "https://open.spotify.com/track/0zR2Rhtz0zvlbD6YF8rEpr"),
            ("Samajavaragamana – Ala Vaikunthapurramuloo", "https://open.spotify.com/track/7jY52hJ4yYBWDdKijOScCe"),
            ("Magic Shop – BTS", "https://open.spotify.com/track/0L5GV9WdYk0UId15zGJo2k"),
            ("Lonely Boy – TXT", "https://open.spotify.com/track/5jOPM80n8c2G8xLU7CGPg8")
        ],
        "quotes": [
            "You don’t have to control your thoughts. You just have to stop letting them control you. – Dan Millman",
            "Tension is who you think you should be. Relaxation is who you are. – Chinese Proverb"
        ],
        "gif": "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif"
    },

    "Calm": {
        "songs": [
            ("Raabta – Agent Vinod", "https://open.spotify.com/track/6HfO6yFAVuZTgTIbKBc3rL"),
            ("Tum Mile (Reprise) – Tum Mile", "https://open.spotify.com/track/1MSpRVjD5MtoHCU9UoWhU5"),
            ("Vellipomaakey – Sahasam Swasaga Sagipo", "https://open.spotify.com/track/6KGhNDNqcjRZlRJ0xizRO2"),
            ("Prema Entha Madhuram – Racha", "https://open.spotify.com/track/6MQxDxtxTGzqWodQy0Vjwv"),
            ("Spring Day – BTS", "https://open.spotify.com/track/6uJ51TBcG7zDDtDfZBml3w"),
            ("Nap of a Star – TXT", "https://open.spotify.com/track/4ODdaG7HG7RuI9aYtNMmJP")
        ],
        "quotes": [
            "Calm mind brings inner strength and self-confidence. – Dalai Lama",
            "Peace begins with a smile. – Mother Teresa"
        ],
        "gif": "https://media.giphy.com/media/26gsiCIKW7ANEmxKE/giphy.gif"
    },

    "Dance": {
        "songs": [
            ("Butta Bomma – Ala Vaikunthapurramuloo", "https://open.spotify.com/track/1crBYi5fLBzNcE9Zk9vZgY"),
            ("Ghungroo – War", "https://open.spotify.com/track/3d2gbXsfR0Q2dnTqkZtGZA"),
            ("Ramulo Ramulaa – Ala Vaikunthapurramuloo", "https://open.spotify.com/track/6GKy0zBfSe1PYDnBQ28szr"),
            ("Malhari – Bajirao Mastani", "https://open.spotify.com/track/4yzZLKV9yPwfDyXz4RJbN5"),
            ("Idol – BTS", "https://open.spotify.com/track/7mldq42yDuxiUNb0uYIUI5"),
            ("PUMA – TXT", "https://open.spotify.com/track/6jktA4TyY8Yu1BrLUJOTbT")
        ],
        "quotes": [
            "Dance like nobody’s watching. Love like you’ve never been hurt. – Mark Twain",
            "When in doubt, just dance it out. – Unknown"
        ],
        "gif": "https://media.giphy.com/media/xTiTnpI3HEVJMuG8di/giphy.gif"
    }
}

st.set_page_config(page_title="Mood Recommender", layout="centered")
st.title("🎧 Mood-Based Music & Quote Recommender")
st.markdown("Tell me how you're feeling today, and I’ll set the vibe for you 💫")

mood = st.selectbox("What's your current mood?", list(mood_options.keys()))

if mood:
    mood_data = mood_options[mood]
    song = random.choice(mood_data["songs"])
    quote = random.choice(mood_data["quotes"])
    gif_url = mood_data["gif"]

    st.subheader("🎵 Song for You")
    st.markdown(f"[{song[0]}]({song[1]})")

    st.subheader("💬 Quote to Reflect On")
    st.markdown(f"> *{quote}*")

    st.subheader("🌈 Mood Visual")
    st.image(gif_url, use_column_width=True)

    st.subheader("📝 Journal Box")
    journal = st.text_area("Want to write something about how you feel?", height=200)
    if st.button("Save Journal Entry"):
        with open("mood_journal.txt", "a", encoding="utf-8") as f:
            f.write(f"\n\nMood: {mood}\nEntry: {journal}\n{'-'*30}")
        st.success("Saved your thoughts 💖")
