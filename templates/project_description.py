project_description_template: str = """
<div class="portfolio-modal modal fade" id="portfolioModal{0}" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="close-modal" data-dismiss="modal"><img src="assets/img/close-icon.svg" alt="Close modal" /></div>
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-lg-8">
                        <div class="modal-body">
                            <h2 class="text-uppercase">{1}</h2>
                            <p class="item-intro text-muted">{2}</p>
                            <img class="img-fluid d-block mx-auto" src="assets/img/portfolio/{3}" alt="" />
                            <p>{4}</p>
                            <ul class="list-inline">
                                <li>Date: {5}</li>
                                <li>Category: {6}</li>
                            </ul>
                            <button class="btn btn-primary" data-dismiss="modal" type="button">
                                <i class="fas fa-times mr-1"></i>
                                Close Project
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
"""