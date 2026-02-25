import streamlit as st # type: ignore

# ========== Page Setup ==========
st.set_page_config(page_title="📚 Books Catalog", page_icon="📖", layout="wide")

# ========== Books Data ==========
books = [ 
   
     {   "id": 1,
     "title": "A Whisper in the Bay", "author": "Fiona Baker", "rating": "4.4",
     "image": "https://m.media-amazon.com/images/I/81ONCaLf05L._SY466_.jpg",
     "plot": "A heartwarming small-town romance about fresh starts, family bonds, and finding love where you least expect it—in the cozy coastal charm of Blueberry Bay.",
     "link": "https://www.amazon.com/Whisper-Bay-Chasing-Tides-Book-ebook/dp/B0CV754VP1"},
   
     {"id": 2,
     "title": "There I Find Rest", "author": "Jessie Gussman", "rating": "4.5",
     "image": "https://m.media-amazon.com/images/I/71jdFjcp13L._SL1499_.jpg",
     "plot": "In Strawberry Sands, a single mom seeking healing and a fresh start discovers unexpected hope, faith, and the possibility of love in a small lakeside town.",
     "link": "https://www.amazon.com/There-Strawberry-Sands-Beach-Romance/dp/B0CDNC5BTK"},

     {"id": 3,
     "title": "Stella", "author": "McCall Hoyle", "rating": "4.8",
     "image":"https://res.cloudinary.com/bookbub/image/upload/t_ci_ar_6:9_padded,f_auto,q_auto,dpr_1,c_scale,w_405/v1751323017/pro_pbid_4654238.jpg",
     "plot": "Stella, a retired bomb-sniffing dog, must save a girl with epilepsy. A heartfelt story with important lessons.",
     "link": "https://www.amazon.com/Stella-Mccall-Hoyle/dp/1629729019"},

     {"id": 4,
     "title": "Rocked", "author": "Gillian Archer", "rating": "4.2",
     "image": "https://res.cloudinary.com/bookbub/image/upload/t_ci_ar_6:9_padded,f_auto,q_auto,dpr_1,c_scale,w_405/v1735898634/pro_pbid_5778525.jpg",
     "plot": "After a wild Vegas night, Shay wakes up married to rock star Chase. Can they turn their impulsive union into real love?",
     "link": "https://www.amazon.com/Rocked-Gods-Rock-Romance-Stars-ebook/dp/B0CBVYNPP9"},

     {"id": 5,
     "title": "Baking in the American South", "author": "Anne Byrn", "rating": "4.8",
     "image": "https://m.media-amazon.com/images/I/81EpjM7AXaL._SY385_.jpg",
     "plot": "Baking in the American South showcases classic Southern recipes and their rich cultural history.",
     "link": "https://www.amazon.com/Baking-American-South-Definitive-Southern/dp/0785291334"},

     {"id": 6,
     "title": "Food52 Genius Recipes", "author": "Kristen Miglore", "rating": "4.6",
     "image": "https://m.media-amazon.com/images/I/81lG5Pj7Z0L._SY385_.jpg",
     "plot": "Genius Recipes shares 100 brilliant, foolproof recipes that inspire and transform home cooking.",
     "link": "https://www.amazon.com/Food52-Genius-Recipes-That-Change/dp/1607747979"},

     {"id": 7,
     "title": "Familiaris", "author": "David Wroblewski", "rating": "4.5",
     "image": "https://m.media-amazon.com/images/I/81W-Zn+iNML._SY522_.jpg",
     "plot": "Familiaris tells the Sawtelle family’s origin, mixing love, family, and the bond between humans and dogs.",
     "link": "https://www.amazon.com/Familiaris-David-Wroblewski-ebook/dp/B0CQ3P6BBT"},

     {"id": 8,
     "title": "To Have And To Hold", "author": "Lily Michaels", "rating": "3.9",
     "image": "https://m.media-amazon.com/images/I/71COKUNZKnL._SY522_.jpg",
     "plot": "To Have and To Hold is a Pride and Prejudice variation exploring love, family, and personal growth.",
     "link": "https://www.amazon.com/Have-Hold-Pride-Prejudice-Variation-ebook/dp/B0FHWW4FGC"},

     {"id": 9,
     "title": "Pardon of Innocence", "author": "Michael Flynn", "rating": "3.9",
     "image": "https://m.media-amazon.com/images/I/71XBZTqCQbL._SY466_.jpg",
     "plot": "Pardon of Innocence is Michael T. Flynn’s memoir of service, struggle, and redemption.",
     "link": "https://www.amazon.com/Pardon-Innocence-Inspiring-Story-Freedom/dp/B0DXD5KGPN"},

     {"id": 10,
     "title": "A Dime to Say I Love You", "author": "Kathryn Henry", "rating": "4.6",
     "image": "https://m.media-amazon.com/images/I/91+OK1eKlfL._SY466_.jpg",
     "plot": "A Dime to Say I Love You is a memoir of love, loss, and spiritual healing.",
     "link": "https://www.amazon.com/Dime-Say-Love-You-Spiritual-ebook/dp/B0F74K3Y1J"},

     {"id": 11,
     "title": "Room 27", "author": "Ariana Godoy", "rating": "4.6",
     "image": "https://m.media-amazon.com/images/I/910xg4ufThL._SX342_.jpg",
     "plot": "An injured baseball star finds hope through an unexpected bond with a mysterious patient.",
     "link": "https://www.amazon.com/Audible-Room-27-English-Edition/dp/B0F8XGGRWN"},

     {"id": 12,
     "title": "Dream On", "author": "Jennifer Hartmann", "rating": "4.6",
     "image": "https://m.media-amazon.com/images/I/81WGYCseBSL._SL1500_.jpg",
     "plot": "A Hollywood star and a small-town dreamer reunite in a fake romance where past heartbreak meets new desire.",
     "link": "https://www.amazon.com/Dream-Deluxe-Jennifer-Hartmann/dp/1464236399"},
]

# ========== Favorites State ==========
if "favorites" not in st.session_state:
    st.session_state.favorites = []

st.markdown("""
<style>
/* خلفية جذابة */
.stApp {
    background-image: linear-gradient(to right, #ffffff, #a7ffeb);
    background-attachment: fixed;
}

/* العنوان */
h1 {
    text-align: center;
    font-size: 45px;
    margin-top: 0.5rem;
    margin-bottom: 2rem;
    color: #004d40;
}

/* كروت الكتب */
.book-card {
    background: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    text-align: center;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ========== Title ==========
st.markdown("<h1>📚 Books Catalog </h1>", unsafe_allow_html=True)

# ========== Navigation ==========
choice = st.radio(
    "Choose:",
    ["🔍 Search", "📩 Contact", "❤️ Favorites", "📚 All Books"],
    horizontal=True
)

# ========== Function to Display a Book ==========
def display_book(book):
    with st.container():
        st.markdown('<div class="book-card">', unsafe_allow_html=True)

        st.image(book["image"], width=150)
        st.subheader(f"{book['title']} by {book['author']} | ⭐ {book['rating']}")

        # -------- Info Toggle --------
        info_key = f"show_info_{book['id']}"

        if info_key not in st.session_state:
            st.session_state[info_key] = False

        if st.button(f"ℹ️ More Information about {book['title']}", key=f"info_{book['id']}"):
            st.session_state[info_key] = not st.session_state[info_key]

        if st.session_state[info_key]:
            st.write(book["plot"])
            st.markdown(f"[🔗 Link to book]({book['link']})")

        # -------- Favorites Button --------
        is_fav = book["id"] in st.session_state.favorites

        fav_label = "❤️ Remove from Favorites" if is_fav else "🤍 Add to Favorites"

        if st.button(fav_label, key=f"fav_btn_{book['id']}"):

            if is_fav:
                if book["id"] in st.session_state.favorites:
                    st.session_state.favorites.remove(book["id"])
            else:
                st.session_state.favorites.append(book["id"])

# ========== Pages ==========
if choice == "📩 Contact":
    st.info("📧 Official Email: **mariemmomdouh967@gmail.com**")

elif choice == "❤️ Favorites":
    if st.session_state.favorites:
        st.success("📌 Your Favorite Books:")
        cols = st.columns(2)
        for i, fav in enumerate(st.session_state.favorites):
            book = next((b for b in books if b["id"] == fav), None)
            if book:
                with cols[i % 2]:
                    display_book(book)
    else:
        st.warning("❤️ No favorites added yet.")

elif choice == "📚 All Books":
    cols = st.columns(2)  # شبكة من عمودين
    for i, book in enumerate(books):
        with cols[i % 2]:
            display_book(book)

elif choice == "🔍 Search":
    search_query = st.text_input("🔍 Search for a book:")

    if search_query:
        filtered_books = [b for b in books if search_query.lower() in b["title"].lower()]
        if filtered_books:
            cols = st.columns(2)
            for i, book in enumerate(filtered_books):
                with cols[i % 2]:
                    display_book(book)
        else:
            st.error("❌ No book found with that name.")
    else:
        st.info("✍️ Type a word, letter, or full name to search for a book.")

st.markdown("""
<style>
/* خلي الحاوية الخارجية شفافة */
div.stAlert {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}

/* خصص الشكل للمربع الداخلي اللي فيه الكلام */
div.stAlert > div[role="alert"] {
    display: inline-block !important;
    background: #ffffff !important;   /* أبيض */
    color: #000000 !important;        /* كتابة سوداء */
    border: 1px solid #cfd8dc !important;
    border-radius: 10px !important;
    padding: 0.5rem 1rem !important;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.1); /* ظل خفيف */
}
div.stAlert > div[role="alert"] * {
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)







