name1$ = selected$ ("TextGrid")
name2$ = do$("Get tier name...", 7)
fileName$ = name1$ + "-" + name2$ + ".csv"
writeInfoLine: fileName$
writeFile(fileName$, "")
n = do("Get number of intervals...", 7)
for i to n
    label$ = do$("Get label of interval...", 7, i)
    start = do("Get start point...", 7, i)
    end = do("Get end point...", 7, i)
    appendInfoLine: label$, ", ", start, ", ", end
    appendFileLine(fileName$, label$ + "," + string$(start) + "," + string$(end))
endfor