import scrapy

class WeWorkRemotelySpider(scrapy.Spider):
    name = "weworkremotely"
    start_urls = ["https://weworkremotely.com/categories/remote-programming-jobs"]

    def parse(self, response):
        for job in response.css("li.new-listing-container"):
            title = job.css("h4.new-listing__header__title::text").get()
            company = job.css("p.new-listing__company-name::text").get()
            location = job.css("p.new-listing__company-headquarters::text").get(default="Remote").strip()
            link = response.urljoin(job.css("a::attr(href)").get())

            # Extract additional details
            categories = job.css("p.new-listing__categories__category::text").getall()
            employment_type = next((c for c in categories if "Full-Time" in c or "Part-Time" in c), "Unknown")
            salary = next((c for c in categories if "$" in c), "Not Specified")

            # Yield structured data
            yield {
                "title": title.strip() if title else "Unknown",
                "company": company.strip() if company else "Unknown",
                "location": location if location else "Remote",
                "link": link,
                "employment_type": employment_type,
                "salary": salary
            }

            self.logger.info(f"Scraped: {title} at {company} ({location}) - {employment_type}, {salary}")

