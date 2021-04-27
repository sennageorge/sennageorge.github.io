project_thumbnail_template: str = """
<div class="col-lg-4 col-sm-6 mb-4">
    <div class="portfolio-item">
        <a class="portfolio-link" data-toggle="modal" href="#portfolioModal{0}">
            <div class="portfolio-hover">
                <div class="portfolio-hover-content"><i class="fas fa-plus fa-3x"></i></div>
            </div>
            <img class="img-fluid" src="assets/img/portfolio/{1}" alt="" />
        </a>
        <div class="portfolio-caption">
            <div class="portfolio-caption-heading">{2}</div>
            <div class="portfolio-caption-subheading text-muted">{3}</div>
        </div>
    </div>
</div>
"""