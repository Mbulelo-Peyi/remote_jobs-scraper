import pytest
from scrapy.http import HtmlResponse
from remote_jobs.spiders.weworkremotely_spider import WeWorkRemotelySpider


def test_spider_parses_jobs():
    spider = WeWorkRemotelySpider()

    # Use HTML that matches the actual site's structure
    html_content = """
    <ul>
        <li class="new-listing-container">
            <a href="/jobs/123-job">
                <h4 class="new-listing__header__title">Software Engineer</h4>
                <p class="new-listing__company-name">Tech Corp</p>
                <p class="new-listing__company-headquarters">Remote</p>
                <p class="new-listing__categories__category">Full-Time</p>
                <p class="new-listing__categories__category">$100,000</p>
            </a>
        </li>
    </ul>
    """

    response = HtmlResponse(url="https://weworkremotely.com", body=html_content, encoding="utf-8")
    results = list(spider.parse(response))

    # Debugging output
    print("Parsed results:", results)  

    assert len(results) == 1, f"Expected 1 job, but got {len(results)}"
    assert results[0]["title"] == "Software Engineer"
    assert results[0]["company"] == "Tech Corp"
    assert results[0]["location"] == "Remote"
    assert results[0]["link"] == "https://weworkremotely.com/jobs/123-job"
    assert results[0]["employment_type"] == "Full-Time"
    assert results[0]["salary"] == "$100,000"
