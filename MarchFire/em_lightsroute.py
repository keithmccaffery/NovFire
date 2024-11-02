@app.route("/em_lights", methods=["POST", "GET"])
def em_lights():
    if request.method == "POST":
        light = request.form.get("light")
        light_fault = request.form.get("light_fault")
        comment = request.form.get("comment")
        image_url = request.form.get("imageUrl")
        if not image_url:
            print("No image URL provided")
        # rest of your code...
        # Handle the error appropriately
    fault = ''
    remedy = ''

    if request.method == "POST":
        RESULTS[light] = light_fault
        ic(light_fault)
        ic(type(light_fault))
        fault = ''
        remedy = ''
        faultDict = ()
        faultStr = {}

        remedyDict = ()
        remedyStr = {}

        # This is working as expected but I have kept the ic views which helped to solve the problem of getting
        # the strings for the faults and the remedies out of the selection results.
        fault=db.execute("SELECT fault FROM em_lightfixes WHERE fault_id = :light_fault", light_fault=light_fault)
        if fault:
            faultDict = fault[0]
            faultStr = faultDict['fault']
            fault = faultStr
        else:
            print("No fault found for the given light_fault")
        remedy=db.execute("SELECT remedy FROM em_lightfixes WHERE fault_id = :light_fault", light_fault=light_fault)
        if remedy:
            remedyDict = remedy[0]
            remedyStr = remedyDict['remedy']
            remedy = remedyStr
        else:
            print("No remedy found for the given light_fault")
        # The strings were saved into these variables to build the results table below. I have left some of the
        # "debugging tools" that I used to see what was being passed around.
        
        