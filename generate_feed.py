import os
import datetime
import xml.etree.ElementTree as ET

# Configuration
BASE_URL = "https://archive.rthk.hk/mp3/radio/archive/radio1/hktoday/m4a/"  # replace with actual base URL
IMAGE_URL = "https://podcast.rthk.hk/podcast/upload_photo/item_photo/1400x1400_916.jpg"
FEED_TITLE = "晨早新聞天地"
FEED_LINK = BASE_URL
FEED_DESCRIPTION = "新聞天地"
OUTPUT_FILE = "feed.xml"

def generate_feed():
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = FEED_TITLE
    ET.SubElement(channel, "link").text = FEED_LINK
    ET.SubElement(channel, "description").text = FEED_DESCRIPTION

    image = ET.SubElement(channel, "image")
    ET.SubElement(image, "url").text = IMAGE_URL
    ET.SubElement(image, "title").text = FEED_TITLE
    ET.SubElement(image, "link").text = FEED_LINK

    # Generate items for the last 30 days
    today = datetime.date.today()
    for i in range(3):
        date = today - datetime.timedelta(days=i)
        filename = date.strftime("%Y%m%d") + ".m4a"
        url = BASE_URL + filename

        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = f"Episode {date.isoformat()}"
        ET.SubElement(item, "enclosure", url=url, type="audio/mpeg")
        ET.SubElement(item, "guid").text = url
        ET.SubElement(item, "pubDate").text = date.strftime("%a, %d %b %Y 07:11:00 +0800")

    tree = ET.ElementTree(rss)
    tree.write(OUTPUT_FILE, encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    generate_feed()
