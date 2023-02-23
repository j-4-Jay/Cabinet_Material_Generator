from tkinter import *
import tkinter.messagebox as m
import math


# ********
# HELP Button Function
def helper():
	m.showinfo(title="CMG Software Help", message=" ....Cabinet Material Generator.... \
               \n ****************\
               \n HELP\
               \n ****************\
               \n Easy 123 Steps To Generate Material Quantity and Estimate \
               \n ****************\
               \n 1. Enter The Cost Prices and the desired Margin to get the Sell Price.\
               \n 2. Enter the Dimension of the Cabinet and no. of shelves, drawers & Partitions in mm and PCs. respectively\
               \n 3. Get the result by clicking CALCULATE OUTPUT Button")


# ********
# Sell Price Calculation Button Function
sp_18mmBSB = 0
sp_6mmBSB = 0
sp_18mmOSR = 0
sp_FFShutter = 0
sp_HFShutter = 0
sp_LaborCharge = 0


def sp_Calc():
	global sp_18mmBSB
	sp_18mmBSB = (cp_18mmBSB.get() + ((cp_18mmBSB.get() * margin_18mmBSB.get()) / 100))
	global sp_6mmBSB
	sp_6mmBSB = (cp_6mmBSB.get() + ((cp_6mmBSB.get() * margin_6mmBSB.get()) / 100))
	global sp_18mmOSR
	sp_18mmOSR = (cp_18mmOSR.get() + ((cp_18mmOSR.get() * margin_18mmOSR.get()) / 100))
	global sp_FFShutter
	sp_FFShutter = (cp_FFShutter.get() + ((cp_FFShutter.get() * margin_FFShutter.get()) / 100))
	global sp_HFShutter
	sp_HFShutter = (cp_HFShutter.get() + ((cp_HFShutter.get() * margin_HFShutter.get()) / 100))
	global sp_LaborCharge
	sp_LaborCharge = (cp_LaborCharge.get() + ((cp_LaborCharge.get() * margin_LaborCharge.get()) / 100))

	lbl_sp_18mmBSB.configure(text="₹ " + str(sp_18mmBSB))
	lbl_sp_6mmBSB.configure(text="₹ " + str(sp_6mmBSB))
	lbl_sp_18mmOSR.configure(text="₹ " + str(sp_18mmOSR))
	lbl_sp_FFShutter.configure(text="₹ " + str(sp_FFShutter))
	lbl_sp_HFShutter.configure(text="₹ " + str(sp_HFShutter))
	lbl_sp_LaborCharge.configure(text="₹ " + str(sp_LaborCharge))


# ********
# Output Calculation Button Function
def Output_Calc():
	Quantity_output_18mmBSB = math.ceil((LP_sft_calc() + RP_sft_calc()) / 32)
	lbl_Quantity_output_18mmBSB.configure(text=Quantity_output_18mmBSB)

	cp_output_18mmBSB = math.ceil(Quantity_output_18mmBSB * 32 * cp_18mmBSB.get())
	lbl_cp_output_18mmBSB.configure(text=cp_output_18mmBSB)

	sp_output_18mmBSB = math.ceil(Quantity_output_18mmBSB * 32 * sp_18mmBSB)
	lbl_sp_output_18mmBSB.configure(text=sp_output_18mmBSB)

	Quantity_output_6mmBSB = math.ceil(BACK_sft_calc() / 32)
	lbl_Quantity_output_6mmBSB.configure(text=Quantity_output_6mmBSB)

	cp_output_6mmBSB = math.ceil(Quantity_output_6mmBSB * 32 * cp_6mmBSB.get())
	lbl_cp_output_6mmBSB.configure(text=cp_output_6mmBSB)

	sp_output_6mmBSB = math.ceil(Quantity_output_6mmBSB * 32 * sp_6mmBSB)
	lbl_sp_output_6mmBSB.configure(text=sp_output_6mmBSB)

	Quantity_output_18mmOSR = math.ceil((LP_sft_calc() + RP_sft_calc()) / 32)
	lbl_Quantity_output_18mmOSR.configure(text=Quantity_output_18mmOSR)

	cp_output_18mmOSR = math.ceil(Quantity_output_18mmOSR * 32 * cp_18mmOSR.get())
	lbl_cp_output_18mmOSR.configure(text=cp_output_18mmOSR)

	sp_output_18mmOSR = math.ceil(Quantity_output_18mmOSR * 32 * sp_18mmOSR)
	lbl_sp_output_18mmOSR.configure(text=sp_output_18mmOSR)

	Quantity_output_FFShutter = math.ceil((LP_sft_calc() + RP_sft_calc()) / 32)
	lbl_Quantity_output_FFShutter.configure(text=Quantity_output_FFShutter)

	cp_output_FFShutter = math.ceil(Quantity_output_FFShutter * 32 * cp_FFShutter.get())
	lbl_cp_output_FFShutter.configure(text=cp_output_FFShutter)

	sp_output_FFShutter = math.ceil(Quantity_output_FFShutter * 32 * sp_FFShutter)
	lbl_sp_output_FFShutter.configure(text=sp_output_FFShutter)

	Quantity_output_HFShutter = math.ceil((LP_sft_calc() + RP_sft_calc()) / 32)
	lbl_Quantity_output_HFShutter.configure(text=Quantity_output_HFShutter)

	cp_output_HFShutter = math.ceil(Quantity_output_HFShutter * 32 * cp_HFShutter.get())
	lbl_cp_output_HFShutter.configure(text=cp_output_HFShutter)

	sp_output_HFShutter = math.ceil(Quantity_output_HFShutter * 32 * sp_HFShutter)
	lbl_sp_output_HFShutter.configure(text=sp_output_HFShutter)

	Quantity_output_LaborCharge = 1
	lbl_Quantity_output_LaborCharge.configure(text=Quantity_output_LaborCharge)

	cp_output_LaborCharge = math.ceil(Quantity_output_LaborCharge * 32 * cp_LaborCharge.get())
	lbl_cp_output_LaborCharge.configure(text=cp_output_LaborCharge)

	sp_output_LaborCharge = math.ceil(Quantity_output_LaborCharge * 32 * sp_LaborCharge)
	lbl_sp_output_LaborCharge.configure(text=sp_output_LaborCharge)

	sp_output_Total = (
				sp_output_18mmBSB + sp_output_6mmBSB + sp_output_18mmOSR + sp_output_FFShutter + sp_output_HFShutter)
	lbl_sp_output_Total.configure(text=sp_output_Total)

	cp_output_Total = (
				cp_output_18mmBSB + cp_output_6mmBSB + sp_output_18mmOSR + cp_output_FFShutter + cp_output_HFShutter)
	lbl_cp_output_Total.configure(text=cp_output_Total)

	Quantity_output_Total = (
				Quantity_output_18mmBSB + Quantity_output_6mmBSB + Quantity_output_18mmOSR + Quantity_output_FFShutter + Quantity_output_HFShutter)
	lbl_Quantity_output_Total.configure(text=Quantity_output_Total)

	cab_sft_calc = int(FRONT_sft_calc())
	lbl_cab_sft_calc.configure(text=cab_sft_calc)

	shutter_expSide_sft_calc = FRONT_sft_calc()
	profit_calc = FRONT_sft_calc


# ********
# Main Window Creation
MainWindow = Tk()
MainWindow.title("Cabinet Material Generator(CMG)")
MainWindow.geometry("408x725")
MainWindow.configure(bg="white")
MainWindow.resizable(True, True)
logo_icon = PhotoImage(file="D:\Work\Python\All_Python_Projects_Jay\Personal_Codes\Cabinet_Material_Generator\CI Logo_16.2.21 copy.png")
MainWindow.iconphoto(True, logo_icon)

# ********
# Declaring all text_variables for button command calculations

sp_18mmBSB = str()
cp_18mmBSB = IntVar()
margin_18mmBSB = IntVar()

sp_6mmBSB = str()
cp_6mmBSB = IntVar()
margin_6mmBSB = IntVar()

sp_18mmOSR = str()
cp_18mmOSR = IntVar()
margin_18mmOSR = IntVar()

sp_FFShutter = str()
cp_FFShutter = IntVar()
margin_FFShutter = IntVar()

sp_HFShutter = str()
cp_HFShutter = IntVar()
margin_HFShutter = IntVar()

sp_LaborCharge = str()
cp_LaborCharge = IntVar()
margin_LaborCharge = IntVar()

CabWidth = IntVar()
CabDepth = IntVar()
CabHeight = IntVar()

Shelves = IntVar()
Partitions = IntVar()
Drawers = IntVar()
Exposed_Sides = IntVar()

sp_output_18mmBSB = str()
cp_output_18mmBSB = str()
Quantity_output_18mmBSB = str()

sp_output_6mmBSB = str()
cp_output_6mmBSB = str()
Quantity_output_6mmBSB = str()

sp_output_18mmOSR = str()
cp_output_18mmOSR = str()
Quantity_output_18mmOSR = str()

sp_output_FFShutter = str()
cp_output_FFShutter = str()
Quantity_output_FFShutter = str()

sp_output_HFShutter = str()
cp_output_HFShutter = str()
Quantity_output_HFShutter = str()

sp_output_LaborCharge = str()
cp_output_LaborCharge = str()
Quantity_output_LaborCharge = str()

sp_output_Total = IntVar()
cp_output_Total = IntVar()
Quantity_output_Total = IntVar()

cab_sft_calc = IntVar()
shutter_expSide_sft_calc = IntVar()
profit_calc = IntVar()

LP_sft_calc = IntVar()
RP_sft_calc = IntVar()
TOP_sft_calc = IntVar()
BTM_sft_calc = IntVar()
FRONT_sft_calc = IntVar()
BACK_sft_calc = IntVar()
SHELVE_sft_calc = IntVar()
PARTITION_sft_calc = IntVar()


# ********
# Object variable Sft calculation
def LP_sft_calc():
	return int(math.ceil((CabDepth.get() * CabHeight.get()) / 92903.04))


def RP_sft_calc():
	return int(math.ceil((CabDepth.get() * CabHeight.get()) / 92903.04))


def TOP_sft_calc():
	return int(math.ceil((CabDepth.get() * CabWidth.get()) / 92903.04))


def BTM_sft_calc():
	return int(math.ceil((CabDepth.get() * CabWidth.get()) / 92903.04))


def FRONT_sft_calc():
	return int(math.ceil((CabWidth.get() * CabHeight.get()) / 92903.04))


def BACK_sft_calc():
	return int(math.ceil((CabWidth.get() * CabHeight.get()) / 92903.04))


def SHELVE_sft_calc():
	return int(math.ceil((CabDepth.get() * CabWidth.get()) / 92903.04))


def PARTITION_sft_calc():
	return int(math.ceil((CabDepth.get() * CabHeight.get()) / 92903.04))


# RP_sft_calc = (CabDepth.get() * CabHeight.get())/92903.04
# TOP_sft_calc = (CabWidth.get() * CabDepth.get())/92903.04
# BTM_sft_calc = (CabWidth.get() * CabDepth.get())/92903.04
# FRONT_sft_calc = (CabWidth.get() * CabHeight.get())/92903.04
# BACK_sft_calc = (CabWidth.get() * CabHeight.get())/92903.04
# SHELVE_sft_calc = (CabWidth.get() * CabDepth.get())/92903.04
# PARTITION_sft_calc = (CabDepth.get() * CabHeight.get())/92903.04


# ********
# 1st heading and 1st Section Heading
b_Help = Button(MainWindow, text="Click To Know How To Use This Software", width=400, command=helper)
# lbl_Title = Label(MainWindow,text="********",width=44,\
#                font=("comic scan",12,"bold"), height=1)
lbl_SubTitle_01 = Label(MainWindow, text="SELLING PRICE CALCULATION", width=44, \
                        font=("comic scan", 12, "bold"), height=2, bg="green", fg="white", anchor="center")

# ********
# Column Headings of Sell Price Calculation Section
lbl_Particulars = Label(MainWindow, text="Particulars", width=10, height=1, bg="#04CF01", anchor="center",
                        relief="solid")
lbl_CostPrice = Label(MainWindow, text="Cost Price(₹)", width=10, height=1, bg="#04CF01", anchor="center",
                      relief="solid")
lbl_Margin = Label(MainWindow, text="Margin(%)", width=10, height=1, bg="#04CF01", anchor="center", relief="solid")
lbl_SellPrice = Label(MainWindow, text="Sell Price(₹)", width=10, height=1, bg="#04CF01", anchor="center",
                      relief="solid")

# ********
# Sell Price Calculation Section Particulars and Entry and Calculated values
lbl_18mmBSB = Label(MainWindow, text="18mm BSB", width=10, bg="#04CF01", anchor="center", relief="solid")
e_cp_18mmBSB = Entry(MainWindow, textvariable=cp_18mmBSB, width=10, bg="#CDFECC", relief="solid", justify="center")
e_margin_18mmBSB = Entry(MainWindow, textvariable=margin_18mmBSB, width=10, bg="#CDFECC", relief="solid",
                         justify="center")
lbl_sp_18mmBSB = Label(MainWindow, textvariable=sp_18mmBSB, width=10, bg="#04CF01", relief="solid")

lbl_6mmBSB = Label(MainWindow, text="6mm BSB", width=10, height=1, bg="#04CF01", anchor="center", relief="solid")
e_cp_6mmBSB = Entry(MainWindow, textvariable=cp_6mmBSB, width=10, bg="#CDFECC", relief="solid", justify="center")
e_margin_6mmBSB = Entry(MainWindow, textvariable=margin_6mmBSB, width=10, bg="#CDFECC", relief="solid",
                        justify="center")
lbl_sp_6mmBSB = Label(MainWindow, textvariable=sp_6mmBSB, width=10, bg="#04CF01", relief="solid")

lbl_18mmOSR = Label(MainWindow, text="18mm OSR", width=10, height=1, bg="#04CF01", anchor="center", relief="solid",
                    justify="center")
e_cp_18mmOSR = Entry(MainWindow, textvariable=cp_18mmOSR, width=10, bg="#CDFECC", relief="solid", justify="center")
e_margin_18mmOSR = Entry(MainWindow, textvariable=margin_18mmOSR, width=10, bg="#CDFECC", relief="solid",
                         justify="center")
lbl_sp_18mmOSR = Label(MainWindow, textvariable=sp_18mmOSR, width=10, bg="#04CF01", relief="solid")

lbl_FFShutter = Label(MainWindow, text="FF Shutter", width=10, height=1, bg="#04CF01", anchor="center", relief="solid")
e_cp_FFShutter = Entry(MainWindow, textvariable=cp_FFShutter, width=10, bg="#CDFECC", relief="solid", justify="center")
e_margin_FFShutter = Entry(MainWindow, textvariable=margin_FFShutter, width=10, bg="#CDFECC", relief="solid",
                           justify="center")
lbl_sp_FFShutter = Label(MainWindow, textvariable=sp_FFShutter, width=10, bg="#04CF01", relief="solid")

lbl_HFShutter = Label(MainWindow, text="HF Shutter", width=10, height=1, bg="#04CF01", anchor="center", relief="solid")
e_cp_HFShutter = Entry(MainWindow, textvariable=cp_HFShutter, width=10, bg="#CDFECC", relief="solid", justify="center")
e_margin_HFShutter = Entry(MainWindow, textvariable=margin_HFShutter, width=10, bg="#CDFECC", relief="solid",
                           justify="center")
lbl_sp_HFShutter = Label(MainWindow, textvariable=sp_HFShutter, width=10, bg="#04CF01", relief="solid")

lbl_LaborCharge = Label(MainWindow, text="Labor Charge", width=10, height=1, bg="#04CF01", anchor="center",
                        relief="solid")
e_cp_LaborCharge = Entry(MainWindow, textvariable=cp_LaborCharge, width=10, bg="#CDFECC", relief="solid",
                         justify="center")
e_margin_LaborCharge = Entry(MainWindow, textvariable=margin_LaborCharge, width=10, bg="#CDFECC", relief="solid",
                             justify="center")
lbl_sp_LaborCharge = Label(MainWindow, textvariable=sp_LaborCharge, width=10, bg="#04CF01", relief="solid")

# ********
# Sell Price Calculation Button
b_sp_Calc = Button(MainWindow, text="👉🏻 Calculate Selling Price 👈🏻", bg="green", fg="white", width=305, command=sp_Calc)

# ********
# Cabinet Dimension Heading
lbl_SubTitle_02 = Label(MainWindow, text="CABINET DETAILS", width=44, \
                        font=("comic scan", 12, "bold"), height=2, bg="#D86200", anchor="center")

# ********
# Cabinet Dimensions & Details Entry
lbl_CabWidth = Label(MainWindow, text="WIDTH(mm)", width=10, height=1, bg="#FF9C4A", anchor="center", relief="solid")
e_CabWidth = Entry(MainWindow, textvariable=CabWidth, width=10, bg="#FFCA9E", relief="solid", justify="center")

lbl_CabDepth = Label(MainWindow, text="DEPTH(mm)", width=10, height=1, bg="#FF9C4A", anchor="center", relief="solid")
e_CabDepth = Entry(MainWindow, textvariable=CabDepth, width=10, bg="#FFCA9E", relief="solid", justify="center")

lbl_CabHeight = Label(MainWindow, text="HEIGHT(mm)", width=10, height=1, bg="#FF9C4A", anchor="center", relief="solid")
e_CabHeight = Entry(MainWindow, textvariable=CabHeight, width=10, bg="#FFCA9E", relief="solid", justify="center")

lbl_Shelves = Label(MainWindow, text="Shelves", width=10, height=1, bg="#FF9C4A", anchor="center", relief="solid")
e_Shelves = Entry(MainWindow, textvariable=Shelves, width=10, bg="#FFCA9E", relief="solid", justify="center")

lbl_Partitions = Label(MainWindow, text="Partitions", width=10, height=1, bg="#FF9C4A", anchor="center", relief="solid")
e_Partitions = Entry(MainWindow, textvariable=Partitions, width=10, bg="#FFCA9E", relief="solid", justify="center")

lbl_Drawers = Label(MainWindow, text="Drawers", width=10, height=1, bg="#FF9C4A", anchor="center", relief="solid")
e_Drawers = Entry(MainWindow, textvariable=Drawers, width=10, bg="#FFCA9E", relief="solid", justify="center")

lbl_Exposed_Sides = Label(MainWindow, text="Exposed Sides", width=10, height=1, bg="#FF9C4A", anchor="center",
                          relief="solid")
e_Exposed_Sides = Entry(MainWindow, textvariable=Exposed_Sides, width=10, bg="#FFCA9E", relief="solid",
                        justify="center")

# ********
# Output Calculation Button
b_Output_Calc = Button(MainWindow, text="👉🏻 Calculate Output 👈🏻", bg="#CD006A", fg="white", width=305,
                       command=Output_Calc)

# ********
# Output Section
lbl_Output_Particulars = Label(MainWindow, text="Particulars", width=10, height=1, bg="#CD006A", fg="white",
                               anchor="center", relief="solid")
lbl_OutPut_SellPrice = Label(MainWindow, text="Sell Price", width=10, height=1, bg="#CD006A", fg="white",
                             anchor="center", relief="solid")
lbl_OutPut_CostPrice = Label(MainWindow, text="Cost Price", width=10, height=1, bg="#CD006A", fg="white",
                             anchor="center", relief="solid")
lbl_OutPut_Quantity = Label(MainWindow, text="Quantity", width=10, height=1, bg="#CD006A", fg="white", anchor="center",
                            relief="solid")

lbl_output_18mmBSB = Label(MainWindow, text="18mm BSB", width=10, fg="white", bg="#CD006A", anchor="center",
                           relief="solid")
lbl_sp_output_18mmBSB = Label(MainWindow, textvariable=sp_output_18mmBSB, width=10, bg="#FF7FC1", relief="solid")
lbl_cp_output_18mmBSB = Label(MainWindow, textvariable=cp_output_18mmBSB, width=10, bg="#FF7FC1", relief="solid",
                              justify="center")
lbl_Quantity_output_18mmBSB = Label(MainWindow, textvariable=Quantity_output_18mmBSB, width=10, bg="#FF7FC1",
                                    relief="solid", justify="center")

lbl_output_6mmBSB = Label(MainWindow, text="6mm BSB", width=10, fg="white", bg="#CD006A", anchor="center",
                          relief="solid")
lbl_sp_output_6mmBSB = Label(MainWindow, textvariable=sp_output_6mmBSB, width=10, bg="#FF7FC1", relief="solid")
lbl_cp_output_6mmBSB = Label(MainWindow, textvariable=cp_output_6mmBSB, width=10, bg="#FF7FC1", justify="center",
                             relief="solid")
lbl_Quantity_output_6mmBSB = Label(MainWindow, textvariable=Quantity_output_6mmBSB, width=10, bg="#FF7FC1",
                                   justify="center", relief="solid")

lbl_output_18mmOSR = Label(MainWindow, text="18mm OSR", width=10, fg="white", bg="#CD006A", anchor="center",
                           relief="solid")
lbl_sp_output_18mmOSR = Label(MainWindow, textvariable=sp_output_18mmOSR, width=10, bg="#FF7FC1", relief="solid")
lbl_cp_output_18mmOSR = Label(MainWindow, textvariable=cp_output_18mmOSR, width=10, bg="#FF7FC1", relief="solid",
                              justify="center")
lbl_Quantity_output_18mmOSR = Label(MainWindow, textvariable=Quantity_output_18mmOSR, width=10, bg="#FF7FC1",
                                    relief="solid", justify="center")

lbl_output_FFShutter = Label(MainWindow, text="FFShutter", width=10, fg="white", bg="#CD006A", anchor="center",
                             relief="solid")
lbl_sp_output_FFShutter = Label(MainWindow, textvariable=sp_output_FFShutter, width=10, bg="#FF7FC1", relief="solid")
lbl_cp_output_FFShutter = Label(MainWindow, textvariable=cp_output_FFShutter, width=10, bg="#FF7FC1", relief="solid",
                                justify="center")
lbl_Quantity_output_FFShutter = Label(MainWindow, textvariable=Quantity_output_FFShutter, width=10, bg="#FF7FC1",
                                      relief="solid", justify="center")

lbl_output_HFShutter = Label(MainWindow, text="HFShutter", width=10, fg="white", bg="#CD006A", anchor="center",
                             relief="solid")
lbl_sp_output_HFShutter = Label(MainWindow, textvariable=sp_output_HFShutter, width=10, bg="#FF7FC1", relief="solid")
lbl_cp_output_HFShutter = Label(MainWindow, textvariable=cp_output_HFShutter, width=10, bg="#FF7FC1", relief="solid",
                                justify="center")
lbl_Quantity_output_HFShutter = Label(MainWindow, textvariable=Quantity_output_HFShutter, width=10, bg="#FF7FC1",
                                      relief="solid", justify="center")

lbl_output_LaborCharge = Label(MainWindow, text="LaborCharge", width=10, fg="white", bg="black", anchor="center",
                               relief="solid")
lbl_sp_output_LaborCharge = Label(MainWindow, textvariable=sp_output_LaborCharge, width=10, bg="grey", relief="solid")
lbl_cp_output_LaborCharge = Label(MainWindow, textvariable=cp_output_LaborCharge, width=10, bg="grey", relief="solid",
                                  justify="center")
lbl_Quantity_output_LaborCharge = Label(MainWindow, textvariable=Quantity_output_LaborCharge, width=10, bg="grey",
                                        relief="solid", justify="center")

lbl_output_Total = Label(MainWindow, text="Total:", width=10, fg="white", bg="#CD006A", anchor="center", relief="solid")
lbl_sp_output_Total = Label(MainWindow, textvariable=sp_output_Total, width=10, fg="white", bg="#CD006A",
                            relief="solid")
lbl_cp_output_Total = Label(MainWindow, textvariable=cp_output_Total, width=10, fg="white", bg="#CD006A",
                            relief="solid")
lbl_Quantity_output_Total = Label(MainWindow, textvariable=Quantity_output_Total, width=10, bg="#CD006A", fg="white",
                                  relief="solid")

lbl_cab_sft = Label(MainWindow, text="Cabinet Sq.Ft.:", width=21, bg="#004357", fg="white", anchor="e", relief="solid")
lbl_cab_sft_calc = Label(MainWindow, textvariable=cab_sft_calc, width=10, bg="#00C5FF", relief="solid")
lbl_shutter_expSide_sft = Label(MainWindow, text="Shutter + Exp. Sides Sq.Ft.:", width=21, bg="#004357", fg="white",
                                anchor="e", relief="solid")
lbl_shutter_expSide_sft_calc = Label(MainWindow, textvariable=shutter_expSide_sft_calc, width=10, bg="#00C5FF",
                                     relief="solid")
lbl_profit = Label(MainWindow, text="Profit:", width=21, bg="#004357", fg="white", anchor="e", relief="solid")
lbl_profit_calc = Label(MainWindow, textvariable=profit_calc, width=10, bg="#00C5FF", relief="solid")

CI_Logo = PhotoImage(
	file="D:\Work\Python\All_Python_Projects_Jay\Personal_Codes\Cabinet_Material_Generator\CI Logo_70x70.png")
lbl_logo = Label(MainWindow, width=70, height=70, image=CI_Logo)

lbl_version = Label(MainWindow, text="CMG v01....jay", width=10, font=("comic scan", 8, "bold"), height=1, fg="black")

# Grid Placement
b_Help.grid(row=0, column=0, columnspan=45)
lbl_SubTitle_01.grid(row=1, column=0, columnspan=45)

lbl_Particulars.grid(row=2, column=0, pady=1)
lbl_CostPrice.grid(row=2, column=1)
lbl_Margin.grid(row=2, column=2)
lbl_SellPrice.grid(row=2, column=3)

lbl_18mmBSB.grid(row=3, column=0)
e_cp_18mmBSB.grid(row=3, column=1)
e_margin_18mmBSB.grid(row=3, column=2)
lbl_sp_18mmBSB.grid(row=3, column=3)

lbl_6mmBSB.grid(row=4, column=0)
e_cp_6mmBSB.grid(row=4, column=1)
e_margin_6mmBSB.grid(row=4, column=2)
lbl_sp_6mmBSB.grid(row=4, column=3)

lbl_18mmOSR.grid(row=5, column=0)
e_cp_18mmOSR.grid(row=5, column=1)
e_margin_18mmOSR.grid(row=5, column=2)
lbl_sp_18mmOSR.grid(row=5, column=3)

lbl_FFShutter.grid(row=6, column=0)
e_cp_FFShutter.grid(row=6, column=1)
e_margin_FFShutter.grid(row=6, column=2)
lbl_sp_FFShutter.grid(row=6, column=3)

lbl_HFShutter.grid(row=7, column=0)
e_cp_HFShutter.grid(row=7, column=1)
e_margin_HFShutter.grid(row=7, column=2)
lbl_sp_HFShutter.grid(row=7, column=3)

lbl_LaborCharge.grid(row=8, column=0)
e_cp_LaborCharge.grid(row=8, column=1)
e_margin_LaborCharge.grid(row=8, column=2)
lbl_sp_LaborCharge.grid(row=8, column=3)

b_sp_Calc.grid(row=9, column=1, columnspan=45)

lbl_SubTitle_02.grid(row=10, column=0, columnspan=45)

lbl_CabWidth.grid(row=12, column=0, pady=1)
e_CabWidth.grid(row=13, column=0)
lbl_CabDepth.grid(row=12, column=1)
e_CabDepth.grid(row=13, column=1)
lbl_CabHeight.grid(row=12, column=2)
e_CabHeight.grid(row=13, column=2)

lbl_Shelves.grid(row=14, column=0)
e_Shelves.grid(row=15, column=0)
lbl_Partitions.grid(row=14, column=1)
e_Partitions.grid(row=15, column=1)
lbl_Drawers.grid(row=14, column=2)
e_Drawers.grid(row=15, column=2)
lbl_Exposed_Sides.grid(row=14, column=3)
e_Exposed_Sides.grid(row=15, column=3)

b_Output_Calc.grid(row=16, column=1, columnspan=45)

lbl_Output_Particulars.grid(row=17, column=0)
lbl_OutPut_SellPrice.grid(row=17, column=1)
lbl_OutPut_CostPrice.grid(row=17, column=2)
lbl_OutPut_Quantity.grid(row=17, column=3)

lbl_output_18mmBSB.grid(row=18, column=0, pady=1)
lbl_sp_output_18mmBSB.grid(row=18, column=1)
lbl_cp_output_18mmBSB.grid(row=18, column=2)
lbl_Quantity_output_18mmBSB.grid(row=18, column=3)

lbl_output_6mmBSB.grid(row=19, column=0)
lbl_sp_output_6mmBSB.grid(row=19, column=1)
lbl_cp_output_6mmBSB.grid(row=19, column=2)
lbl_Quantity_output_6mmBSB.grid(row=19, column=3)

lbl_output_18mmOSR.grid(row=20, column=0, pady=1)
lbl_sp_output_18mmOSR.grid(row=20, column=1)
lbl_cp_output_18mmOSR.grid(row=20, column=2)
lbl_Quantity_output_18mmOSR.grid(row=20, column=3)

lbl_output_FFShutter.grid(row=21, column=0)
lbl_sp_output_FFShutter.grid(row=21, column=1)
lbl_cp_output_FFShutter.grid(row=21, column=2)
lbl_Quantity_output_FFShutter.grid(row=21, column=3)

lbl_output_HFShutter.grid(row=22, column=0, pady=1)
lbl_sp_output_HFShutter.grid(row=22, column=1)
lbl_cp_output_HFShutter.grid(row=22, column=2)
lbl_Quantity_output_HFShutter.grid(row=22, column=3)

lbl_output_LaborCharge.grid(row=24, column=0)
lbl_sp_output_LaborCharge.grid(row=24, column=1)
lbl_cp_output_LaborCharge.grid(row=24, column=2)
lbl_Quantity_output_LaborCharge.grid(row=24, column=3)

lbl_output_Total.grid(row=23, column=0, pady=1)
lbl_sp_output_Total.grid(row=23, column=1)
lbl_cp_output_Total.grid(row=23, column=2)
lbl_Quantity_output_Total.grid(row=23, column=3)

lbl_cab_sft.grid(row=25, column=0, pady=1, columnspan=2)
lbl_cab_sft_calc.grid(row=25, column=2, pady=1)
lbl_shutter_expSide_sft.grid(row=26, column=0, pady=1, columnspan=2)
lbl_shutter_expSide_sft_calc.grid(row=26, column=2, pady=1)
lbl_profit.grid(row=27, column=0, pady=1, columnspan=2)
lbl_profit_calc.grid(row=27, column=2, pady=1)

lbl_logo.grid(row=25, column=3, rowspan=3, pady=1)

lbl_version.grid(row=28, column=3, pady=1)

MainWindow.mainloop()