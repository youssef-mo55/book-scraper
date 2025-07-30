# 📚 Book Scraper

A simple and powerful web scraper built in Python using `requests`, `BeautifulSoup`, and `pandas` to extract book data from [Books to Scrape](https://books.toscrape.com).

---

## 🚀 Features

* Scrapes multiple pages of books
* Extracts:

  * 📖 Title
  * 💵 Price
  * ✅ Availability
  * ⭐ Rating
  * 📂 Category
  * 📝 Description
  * 🆑 UPC
  * 💰 Price (excl. & incl. tax)
  * 🢾 Tax
  * 📦 Stock
  * 💬 Number of Reviews
  * 🔗 Book URL
* Saves the data to a structured CSV file

---

## 🛠 Technologies Used

* Python 3.x
* `requests`
* `BeautifulSoup` (bs4)
* `pandas`
* `lxml` parser

---

## 📁 Output Example

All data is saved in:

```
All_Books_details.csv
```

Sample row:

| Title                   | Price  | Availability | Rating | Category | ... |
| ----------------------- | ------ | ------------ | ------ | -------- | --- |
| It's Only the Himalayas | £45.17 | In stock     | 2      | Travel   | ... |

---

## 🧠 How It Works

1. Loop through 3 pages of books.
2. Visit each book’s individual page.
3. Extract all metadata safely using BeautifulSoup.
4. Store everything into a list of dictionaries.
5. Save to a CSV file using pandas.

---

## ▶️ How to Run

```bash
# Clone the repo
git clone https://github.com/youssef-mo55/book-scraper.git
cd book-scraper

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python book_scraper.py
```

---

## ✅ Requirements

Make sure you have Python 3.6+ and the required packages:

```bash
pip install requests beautifulsoup4 pandas lxml
```

---

## 📟 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the project and submit suggestions or improvements.

---

## 📬 Contact

Feel free to connect:

* 📧 [yousef@example.com](mailto:ym1190732@gmail.com)
* 🔗 [LinkedIn](www.linkedin.com/in/youssef-mohamed-b37a8427b)
* 📘 [Facebook](https://www.facebook.com/yousef.mohamed.488556)

---

> Built with ❤️ by [Yousef Mohamed](https://github.com/youssef-mo55)
