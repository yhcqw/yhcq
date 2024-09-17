import requests
from bs4 import BeautifulSoup

def extract_info(url, year):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links containing 'yhcq.html'
    links = soup.find_all('a', href=True)
    extracted_info = []

    for link in links:
        if 'yhcq.html' in link['href']:
            # Extract title
            title = link.get_text(strip=True).replace('&quot;', '"')
            print(title)
            
            # Navigate to the link to extract the author
            detail_url = link['href']
            try:
                detail_response = requests.get(detail_url)
                detail_soup = BeautifulSoup(detail_response.content, 'html.parser')
                author_div = detail_soup.find('div', class_='list-author')  # Update class name based on actual HTML
                if author_div:
                    author_span = author_div.find('span', recursive=False)
                    author = author_span.get_text(strip=True).strip() if author_span else "未知"
                else:
                    author = "未知"
                print(author)
            except Exception as e:
                print(f"Error fetching details from {detail_url}: {e}")
                author = "未知"

            # Format and store the extracted information
            extracted_info.append(f"{year} {title}  作者：{author}")

    return extracted_info

def main():
    year = input("Enter the year (format YYYYMM): ")
    base_url = "https://doc.taixueshu.com/journal/yhcq/20109/"  # Base URL
    
    # Extract information
    info_list = extract_info(base_url, year)
    
    # Write to file
    if info_list:
        with open('output.txt', 'w', encoding='utf-8') as file:
            for info in info_list:
                file.write(info + '\n')
        print("Information has been written to output.txt")
    else:
        print("No information found or failed to extract.")

if __name__ == "__main__":
    main()
