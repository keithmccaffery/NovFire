@app.route("/doors", methods=["POST", "GET"])
def doors():
    door = request.form.get("door")
    door_fault = request.form.get("door_fault")
    comment = request.form.get("comment")
    image_url = request.form.get("imageUrl")
    fault = ''
    remedy = ''
    asset = door
    if request.method == "POST":
        RESULTS[door] = door_fault
        ic(door_fault)
        ic(type(door_fault))
        fault = ''
        remedy = ''
        faultDict = ()
        faultStr = {}

        remedyDict = ()
        remedyStr = {}

        # This is working as expected but I have kept the ic views which helped to solve the problem of getting
        # the strings for the faults and the remedies out of the selection results.
        fault=db.execute("SELECT fault FROM doorfixes WHERE fault_id = :door_fault",
                    door_fault=door_fault)
        remedy=db.execute("SELECT remedy FROM doorfixes WHERE fault_id = :door_fault",
                    door_fault=door_fault)
        ic(remedy)
        faultDict   = fault [0]
        faultStr = faultDict  ['fault']

        remedyDict = remedy [0]
        remedyStr= remedyDict  ['remedy']

        # The strings were saved into these variables to build the results table below. I have left some of the
        # "debugging tools" that I used to see what was being passed around.
        remedy = remedyStr
        fault = faultStr


        print(fault)
        print(remedy)

        ic(fault)
        ic(remedy)
        ic(type(fault))
        ic(type(remedy))

        from datetime import datetime

        db.execute("INSERT INTO results (user_id, asset, fault_id, fault, remedy, comment, image_url, timestamp) VALUES (:user_id, :asset, :fault_id, :fault, :remedy, :comment, :image_url, :timestamp)",
                    user_id=session["user_id"], asset=asset, fault_id=door_fault, fault=fault, remedy=remedy, comment=comment, image_url=image_url, timestamp=datetime.now())
       # More remnants of the lines that I  needed to solve the data type
        print(RESULTS[door])
        return redirect("/results")

    else:
        return render_template("doors.html",  door_faults=DOOR_FAULTS)

# These following functions could be completed as per the doors method above, however, since hearing about OOP
# it maybe better to write app.py having classes producing the objects.