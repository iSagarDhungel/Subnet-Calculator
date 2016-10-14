import random 
import sys  
def subnetCalc(): 
    try: 
        print("\n") 
         
        #Checking IP address validity 
        while True: 
            ipAddress = input("Enter an IP address: ") 
             
            #Checking octets             
            a = ipAddress.split('.')      
            if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255): 
                break 
             
            else: 
                print("\nThe IP address is INVALID! Please retry!\n" )
                continue 
         
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0] 
         
        #Checking Subnet Mask validity 
        while True: 
            subnetMask = input("Enter a subnet mask: ") 
            #Checking octets             
            b = subnetMask.split('.') 
             
            if (len(b) == 4) and (int(b[0]) == 255) and (int(b[1]) in masks) and (int(b[2]) in masks) and (int(b[3]) in masks) and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])): 
                break 
             
            else: 
                print("\nThe subnet mask is INVALID! Please retry!\n") 
                continue 
          
        #Algorithm for subnet identification, based on IP and Subnet Mask  
        #Convert mask to binary string 
        maskOctetsPadded = [] 
        maskOctetsDecimal = subnetMask.split(".") 
         
        for octetIndex in range(0, len(maskOctetsDecimal)): 
             
            binaryOctet = bin(int(maskOctetsDecimal[octetIndex])).split("b")[1] 

            if len(binaryOctet) == 8: 
                maskOctetsPadded.append(binaryOctet) 
             
            elif len(binaryOctet) < 8: 
                binaryOctetPadded = binaryOctet.zfill(8) 
                maskOctetsPadded.append(binaryOctetPadded) 
                 
        decimalMask = "".join(maskOctetsPadded) 
        #Example: for 255.255.255.0 => 11111111111111111111111100000000 
         
        #Counting host bits in the mask and calculating number of hosts/subnet 
        noOfZeros = decimalMask.count("0") 
        noOfOnes = 32 - noOfZeros 
        noOfHosts = abs(2 ** noOfZeros - 2) #return positive value for mask /32 
          
         
        #Obtaining wildcard mask 
        wildcardOctets = [] 
        for wOctet in maskOctetsDecimal: 
            wildOctet = 255 - int(wOctet) 
            wildcardOctets.append(str(wildOctet)) 
             
         
        wildcardMask = ".".join(wildcardOctets) 
         
        #Convert IP to binary string 
        ipOctetsPadded = [] 
        ipOctetsDecimal = ipAddress.split(".") 
         
        for octetIndex in range(0, len(ipOctetsDecimal)): 
             
            binaryOctet = bin(int(ipOctetsDecimal[octetIndex])).split("b")[1] 
             
            if len(binaryOctet) < 8: 
                binaryOctetPadded = binaryOctet.zfill(8) 
                ipOctetsPadded.append(binaryOctetPadded) 
             
            else: 
                ipOctetsPadded.append(binaryOctet) 
         
        binaryIp = "".join(ipOctetsPadded) 
        #Example: for 192.168.2.100 => 11000000101010000000001001100100 
         
         
        networkAddressBinary = binaryIp[:(noOfOnes)] + "0" * noOfZeros 
        broadcastAddressBinary = binaryIp[:(noOfOnes)] + "1" * noOfZeros 
 
        netIpOctets = [] 
        for octet in range(0, len(networkAddressBinary), 8): 
            netIpOctet = networkAddressBinary[octet:octet+8] 
            netIpOctets.append(netIpOctet) 
         
        netIpAddress = [] 
        for eachOctet in netIpOctets: 
            netIpAddress.append(str(int(eachOctet, 2))) 

         
        networkAddress = ".".join(netIpAddress) 
         
        bstIpOctets = [] 
        for octet in range(0, len(broadcastAddressBinary), 8): 
            bstIpOctet = broadcastAddressBinary[octet:octet+8] 
            bstIpOctets.append(bstIpOctet) 
                  
        bstIpAddress = [] 
        for eachOctet in bstIpOctets: 
            bstIpAddress.append(str(int(eachOctet, 2))) 
             
         
        broadcastAddress = ".".join(bstIpAddress) 
         
        #Results for selected IP/mask 
        print("\n") 
        print("Network address is: %s" % networkAddress) 
        print("Broadcast address is: %s" % broadcastAddress) 
        print("Number of valid hosts per subnet: %s" % noOfHosts) 
        print("Wildcard mask: %s" % wildcardMask )
        print("Mask bits: %s" % noOfOnes) 
        print("\n") 
         
        
    except KeyboardInterrupt: 
        print("\n\nProgram Interupted\nExiting\n") 
        sys.exit() 
         
#Calling the function 
subnetCalc()
