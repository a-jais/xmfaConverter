'''
Copyright (C) 2015 by Astha Jaiswal
astha421@gmail.com

This file is part of xmfaGenerator.

    xmfaGenerator is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    xmfaGenerator is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with xmfaGenerator. If not, see <http://www.gnu.org/licenses/>.
'''
def convertFiles(fileI, fileO):
        ifl = open(fileI, 'r')
        addiStr = 'position'
        tst=[]
        # remove blank lines???
	maxCount = 0
	firstPass=True
        for line in ifl:
		if(firstPass == True):
                	if not line.startswith(' '):
				maxCount+=1
                        	tst.append(str.split(line))
			else:
				firstPass = False
		else:
                        if not line.startswith(' '):
                                tst.append(str.split(line))

        maxCount=maxCount-3
        tst.pop(0)
        tst.pop(0)
        tst.pop(0)
        
        # remove all the '-'
        count =-1
        finalString = []
        index = 0
        for row in tst:
                count=count+1
                tmpString = []
                if count <= maxCount:
                        if len(row)>1:
                            for col in row[1]:
                                    tmpString.append(col)
                            finalString.append(tmpString)
                else:
                        if len(row)>1:
                            for col in row[1]:
                                    finalString[index].append(col)
                            index = index +1
                            if(index == maxCount):
                                    index=0

        # Now aggregate all the letters for a name. Do this for all the names
        fst = []
        fst = finalString
        ofl = open(fileO, 'w')

        for count1 in range(0, maxCount):
                ofl.write("{}>{}".format('', tst[count1][0]))
                ofl.write("\n")
                for count in range(0, len(fst[0])):
                        ofl.write("{}{}".format('', fst[count1][count]))
                ofl.write("\n")
        ofl.close()
        return "done"
