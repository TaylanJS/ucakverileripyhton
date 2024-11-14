import requests
from bs4 import BeautifulSoup

def get_traffic_data(year, month):
    base_url = "https://investor.turkishairlines.com"
    params = {
        "year": year,
        "month": month
    }
    
    response = requests.get(f"{base_url}/tr/aciklamalar/borsa-aciklamalari", params=params)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
       
        traffic_links = [link['href'] for link in soup.find_all('a', href=True) if "Trafik Sonuçları" in link.text] #Araştırıldı
        
        traffic_data = []
        for link in traffic_links:
            if not link.startswith("http"):#Araştırıldı
                link = base_url + link
            
            report_response = requests.get(link)
            
            if report_response.status_code == 200:
                report_soup = BeautifulSoup(report_response.text, 'html.parser')#Araştırıldı
                
                
                wrapper_bodies = report_soup.find_all(class_="wrapper-body")
                
                if len(wrapper_bodies) > 1:
                    
                    text_content = wrapper_bodies[1].get_text(separator="\n").strip()#Araştırıldı
                    
                  
                    filtered_lines = [line for line in text_content.splitlines() if "tweet" not in line.lower()]#Araştırıldı
                    
                   
                    cleaned_text = "\n".join(line.strip() for line in filtered_lines if line.strip())#Araştırıldı
                    traffic_data.append(cleaned_text)
                else:
                    traffic_data.append("İkinci wrapper-body sınıfı bulunamadı.")
            else:
                print(f"Bu linkten veri alınamadı: {link}")
        
        return traffic_data
    else:
        print(f"Sayfa yüklenemedi: Yıl {year}, Ay {month}")
        return []

def fetch_all_traffic_data(start_year, end_year, end_month):
    all_data = {}
    months = [str(i).zfill(2) for i in range(1, 13)]
    
    for year in range(start_year, end_year + 1):
        for month in months:
            if year == end_year and month > end_month:
                break  
            
            print(f"{year} yılının {month}. ayı için veri alınıyor...")
            traffic_data = get_traffic_data(year, month)
            
            if traffic_data:
                all_data[f"{year}-{month}"] = traffic_data
    
    return all_data


all_traffic_data = fetch_all_traffic_data(2013, 2014, "12")


for date, reports in all_traffic_data.items():
    print(f"Tarih: {date}")
    for i, report in enumerate(reports, 1):
        print(f"Trafik Raporu {i}:\n{report}\n")
