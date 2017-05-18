            cursorProject.execute(""" select key,Project_Name, Project_Number, Project_Folder,Add_Comments, Icon from Projects """)

            for row in cursorProject.fetchall():
                Project = {'Project_Name':[],'Project_Number':[],'Project_Folder':[],'Comments':[],'icon':[]}
                dueDates = {'Description':[],'Dates':[]}
                allContacts = {'contactName':[],'contactNumber':[],'title':[]}
                key,projectName,ProjectNumber,ProjectFolder,Comments,Icon = row
                Project['Project_Name'].append(projectName)
                Project['Project_Number'].append(ProjectNumber)
                Project['Project_Folder'].append(ProjectFolder)
                Project['Comments'].append(Comments)
                Project['icon'].append(Icon)

                cursorProject.execute(""" select Contact_Name, Contact_PhoneNumber from Contacts where Main_Contact = 1 and Project = ?""", (key,))
                MaincontactName,MaincontactNumber = cursorProject.fetchone()

                cursorProject.execute(""" select Contact_Name, Contact_PhoneNumber,Title from Contacts where Project = ?""", (key,))
                for contacts in cursorProject.fetchall():
                    contactName,contactNumber,title = contacts
                    allContacts['contactName'].append(contactName)
                    allContacts['contactNumber'].append(contactNumber)
                    allContacts['title'].append(title)

                cursorProject.execute(""" select Description, Due_Date from DueDates where Project = ?""", (key,))
                for dateRow in cursorProject.fetchall():
                    Desc,DueDate = dateRow
                    dueDates['Description'].append(Desc)
                    dAll = datetime.datetime.strptime(DueDate, '%Y-%m-%d')
                    dueDates['Dates'].append(dAll)

                Project.update({'MaincontactName':MaincontactName,'MaincontactNumber':MaincontactNumber,'Contacts':allContacts,'Due_Dates':dueDates})

                Projects.update({ProjectNumber:Project})


            #INSERT INTO "main"."Projects" ("Project_Name","Project_Number","Project_Folder","Add_Comments") VALUES (?1,?2,?3,?4)
