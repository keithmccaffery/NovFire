# FIRE INSPECTION FOR ANNUAL FIRE SAFETY STATEMENT
#### Video Demo: https://youtu.be/825a5EleiqI
#### Description:

Building inspection is an important process in being able to produce and endorse an Annual Fire Statement that is displayed for all people in the building to see. My project is a python web application that assists the fire inspector in identifying an assets in the building that have to be repaired or replaced in order to issue the Annual Fire Safety Statement. In my home state of New South Wales assets are inspected every six months and the Statement issued annually.

The aim of this project is two fold. Firstly to assist the inspector by having all the evaluation criteria listed that is needed to achieve a complient asset, for example a fire resistant door. Secondly, it is able to easily log into a database any asset that needs to be repaired of replaced. The information stored in the results table can then be used to produce a report on the building that is used to inform the building owners what needs to be done to make these assets complient. The final report can also be used to inform the relevant technicians how to proceed if required.

At this stage of development only a few of the asset classes, namely, fire doors, fire extinguishers and emergency lighting have been included in the scope of web application and only fire doors in operational  with all the evaluation criteria imported to a SQLite database. This database along with the evaluation criteria includes both the fault and the remedy required once a problem is logged. Obviously, the other asset classes need their own table of evaluation criteria, fault description and remedy required. The logic and processes for the door section are otherwise the same.

The fire asset inpector also has the ability to put their own input into the applicaiton if applicable and these comments are then included in the final report on the building. This report also needs the ability to show an image of the problem with the failed asset. This is another of the TO DO items to make this application more effective. Currently I have just used a placeholder image to help imagine how the report may be used. The idea is to have access to the camera of the mobile device being used for the inspection. As it has been said "one picture is worth a thousand words".

Operationally I envisage that the inspector could use a system of numbered stickers that would be placed on the failed asset and that this number would be recorded in the "identity" field on the input form. However, there is also potential to have a database of assets that had been previously identified and recorded depending on the needs of the fire inspector and/or the building owner. However, I believe that my project, which will help me in my role of inspecting these assets, is already complex enough for submission and evaluation.

In regard to some of the

#### Development of the project

I produced a csv file with the Australian standards for assessing the fire doors. This file also include the fault and remedy to fix that fault if the standard was not achieved. This data was imported and converted to a table in the final.db database.

I utilized the base of the CS50 finance project to enable registation and sign in. However rather than registering different users I envisioned that it would be better to register each building and therefore be able to extract that buildings results from the database following the inspection. This works well in my project.

The next consideration was the method of selecting the failed criteria. At first I tried the checkbox option but finally decised the select method with the drop down box was more appropiate. It allowed the entire evaluation criteria to be seen and the asset judged against. The progam promts the user to evaluate all the criteria as an asset may have more than one defect. These faults are recorded and reported seperately as different technician could need to be engaged to retify the defects.

Consideration was given to extracting the appropriate string (the value) only from the table and not the whole dictionary. This was achieved by investigating using the ic command and the ic type command. The program works as expected and inserts only the appropriate string into the results table where they can then be used in the final report. Further enhancement of the application would have it being able to produce a pdf document from it final report. If required this document could be further polished or modified before being released to the building owners and/or technicians engaged to undertake the repairs.

Overall I believe that this was a worthwhile project as it streamlines the work of the Fire Safety inspector of which I am one. Many more enhancements are envisaged for this web application in coming months. Before of the nature application only minimal effort was directed towards styling as compared to getting the logic and results correct.

This is my CS50 final project.
