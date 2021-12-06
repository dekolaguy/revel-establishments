import src as app


def save_establishments(request):
    data = request.get_json()
    state = data.get("state")
    secrets = data.get("secrets")
    # return app.save_productmix_summary(state, secrets)
    return app.save_establishment(state, secrets)
