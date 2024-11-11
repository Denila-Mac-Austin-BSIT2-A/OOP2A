submit_btn=Button(root,text="Add Record to Database", command=submit)
submit_btn.grind(row=6,
                 column=0,
                 columnspan=2,
                 pady=10,
                 pad=10,
                 ipadx=100)

query_btn=Button(root,text="Show Records", command=query)
query_btn.grind(row=7,
                column=0,
                columnspan=2,
                pady=10,
                pad=10,
                ipadx=137)
