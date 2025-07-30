import requests
import pandas as pd
import time
from bs4 import BeautifulSoup


all_books_details = []

for page in range(1, 4):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    print(f"📄 Scraping Page {page}...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        books = soup.find_all('article', class_="product_pod")
    except Exception as e:
        print(f"❌ Error loading page {page}: {e}")
        continue

    for book in books:
        try:
            title = book.h3.a['title']
            price = book.find('p', class_="price_color").text.strip()
            availability = book.find('p', class_="instock availability").text.strip()
            
            rating_tag = book.find('p', class_="star-rating")
            rating_class = rating_tag.get('class')
            rating_text = [c for c in rating_class if c != 'star-rating'][0]
            ratings_map = {
                "One": 1,
                "Two": 2,
                "Three": 3,
                "Four": 4,
                "Five": 5
            }
            rating = ratings_map.get(rating_text, 0)

            relative_url = book.h3.a['href']
            full_url = "https://books.toscrape.com/catalogue/" + relative_url.replace('../../../', '')

            detail_response = requests.get(full_url)
            detail_response.raise_for_status()
            detail_soup = BeautifulSoup(detail_response.text, 'lxml')

            desc = detail_soup.select_one('#product_description + p')
            description = desc.text.strip() if desc else "No description"

            category = detail_soup.select("ul.breadcrumb li a")[-1].text.strip()

            def extract_text(label):
                cell = detail_soup.find('th', string=label)
                return cell.find_next_sibling("td").text.strip() if cell else "N/A"

            upc = extract_text("UPC")
            product_type = extract_text("Product Type")
            price_excl = extract_text("Price (excl. tax)")
            price_incl = extract_text("Price (incl. tax)")
            tax = extract_text("Tax")
            availability_in_book = extract_text("Availability")
            number_of_reviews = extract_text("Number of reviews")

            all_books_details.append({
                "Title": title,
                "Price": price,
                "Availability": availability,
                "Rating": rating,
                "Description": description,
                "Category": category,
                "UPC": upc,
                "Product Type": product_type,
                "Price (excl. tax)": price_excl,
                "Price (incl. tax)": price_incl,
                "Tax": tax,
                "Stock": availability_in_book,
                "Number of Reviews": number_of_reviews,
                "Book URL": full_url
            })

            print(f"✅ Done: {title}")
            time.sleep(0.5)

        except Exception as e:
            print(f"⚠️ Skipped a book due to error: {e}")
            continue

    time.sleep(1)

df = pd.DataFrame(all_books_details)
df.to_csv("All_Books_details2.csv", index=False)
print("📁 Saved to All_Books_details2.csv")
