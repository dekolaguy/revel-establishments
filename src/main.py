import logging

from src.modules.utils import transform_orders
from src.revel.api_handler import APIHandler

logger = logging.getLogger(__name__)


def save_establishment(state, secrets):
    logger.info("Initializing API handler")
    request = APIHandler(secrets.get("baseURL"))

    items = request.request_for_establishments(last_id=state.get("last_item_id"), batch_size=secrets["batch_size"])
    last_item = items[len(items) - 1] if len(items) else None
    filtered_items = transform_orders(items)

    if last_item is not None:
        return_state = {"last_item_id": last_item["id"], "last_item_date": last_item["created_date"]}
    else:
        return_state = state

    return {"insert": {"establishments": filtered_items}, "state": return_state}
