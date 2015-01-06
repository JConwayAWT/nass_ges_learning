#note:  imputed manner of collision is column 4 (indexed at 0)

counter = 0
outfile1 = open("head_on_accidents_without_severity_fit.txt","w") #all the data without severity, made for fitting
outfile2 = open("head_on_accidents_without_severity_test.txt","w") #all the data without, made for testing
outfile3 = open("head_on_accidents_labels_fit.txt","w") #the labels with ALL numbers for severity, made for fitting
outfile4 = open("head_on_accidents_labels_test.txt","w") #the labels with ALL numbers for severity, made for testing
outfile5 = open("head_on_accidents_labels_fatal_fit.txt","w") #the labels as just 1 (fatal) or 0, made for fitting
outfile6 = open("head_on_accidents_labels_fatal_test.txt","w") #the labels as just 1 (fatal) or 0, made for testing
outfile7 = open("head_on_accidents_labels_fatal_or_incapacitating_fit.txt","w") #the labels as 1 (fatal/incap) or 0, made for fitting
outfile8 = open("head_on_accidents_labels_fatal_or_incapacitating_test.txt","w") #the labels as 1 (fatal/incap) or 0, made for testing
outfile9 = open("head_on_accidents_labels_no_injury_fit.txt","w") #labels as 1 (no injury) or 0, made for fitting
outfile10 = open("head_on_accidents_labels_no_injury_test.txt","w") #labels as 1 (no injury) or 0, made for testing
outfile11 = open("head_on_accidents_labels_non_inc_fit.txt", "w") #sim., non-incapacitating injury, made for fitting
outfile12 = open("head_on_accidents_labels_non_inc_test.txt", "w") #sim., non-incapacitating injury, made for testing


with open("accident.txt") as f:
  content = f.readlines()
  for line in content:
    counter += 1
    line_as_array = line.split('\t')
    if line_as_array[4] == '2':
      if counter%2 == 0:
        outfile3.write(line_as_array[34] + '\n')

        if line_as_array[34] == "4":
          outfile5.write("1\n")
        else:
          outfile5.write("0\n")

        if ((line_as_array[34] == "4") or (line_as_array[34] == "3")):
          outfile7.write("1\n")
        else:
          outfile7.write("0\n")

        if line_as_array[34] == "0":
          outfile9.write("1\n")
        else:
          outfile9.write("0\n")

        if line_as_array[34] == "2":
          outfile11.write("1\n")
        else:
          outfile11.write("0\n")

        line_as_array.remove(line_as_array[34])
        line_without_sev = "\t".join(line_as_array)
        outfile1.write(line_without_sev)

      else:
        outfile4.write(line_as_array[34] + '\n')

        if line_as_array[34] == "4":
          outfile6.write("1\n")
        else:
          outfile6.write("0\n")

        if ((line_as_array[34] == "4") or (line_as_array[34] == "3")):
          outfile8.write("1\n")
        else:
          outfile8.write("0\n")

        if line_as_array[34] == "0":
          outfile10.write("1\n")
        else:
          outfile10.write("0\n")

        if line_as_array[34] == "2":
          outfile12.write("1\n")
        else:
          outfile12.write("0\n")

        line_as_array.remove(line_as_array[34])
        line_without_sev = "\t".join(line_as_array)
        outfile2.write(line_without_sev)



outfile1.close()
outfile2.close()
outfile3.close()
outfile4.close()
outfile5.close()
outfile6.close()
outfile7.close()
outfile8.close()
outfile9.close()
outfile10.close()
outfile11.close()
outfile12.close()