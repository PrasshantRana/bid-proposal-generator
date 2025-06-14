def generate_main_body(data):
    """
    This function takes the loaded YAML data,
    uses keys like tender name, bidder name, etc.,
    and returns a professionally written letter body.
    
    (Right now it's a placeholder. You can later use Mistral or OpenAI here.)
    """
    tender_name = data.get("tender_name", "Unknown Tender")
    bidder_name = data.get("bidder_name", "Your Company")

    # Sample static response (replace with AI-generated content later)
    return f"""
    We, {bidder_name}, are pleased to submit our proposal for the {tender_name}.
    We have reviewed the scope and are confident in our ability to meet your expectations.
    """

