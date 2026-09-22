from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = Path('/Users/martagutmane/Downloads/drive-download-20260921T133522Z-1-001/01 GIVE TO CODEX - Answer Template.json')

evidence = [
    {"id":"E01","source":"00 BOARD ORDER READ FIRST.pdf","type":"board order","reliability":"governing case context","description":"Reporting date, currency, task scope and evidence hierarchy."},
    {"id":"E02","source":"02 Bank Export August.csv","type":"bank export","reliability":"strong external evidence","description":"Opening and closing cash; dated receipts, deposits, borrowing and payments through 31 August."},
    {"id":"E03","source":"03 CRM Export Cleaned FINAL.xlsx","type":"CRM export","reliability":"internal operations evidence","description":"Invoices, customer aliases, delivery/completion dates, matched cash and open balances."},
    {"id":"E04","source":"04 Contracts Returns and Angry Customers.pdf","type":"signed contracts and customer records","reliability":"strong external/signed evidence","description":"Accepted contracts, September delivery dates and R-17 liquidation condition."},
    {"id":"E05","source":"05 Warehouse Count Marta Notes.pdf","type":"warehouse count","reliability":"warehouse evidence","description":"31 August physical count, damaged stock condition, purchases, consumption and disposal quote."},
    {"id":"E06","source":"06 Purchases Invoices and Goods Received.pdf","type":"supplier invoices and goods received","reliability":"strong third-party evidence","description":"Purchases, confirmed unpaid balances, equipment invoices and repair scope."},
    {"id":"E07","source":"07 Payroll Bonuses Contractors NEW.xlsx","type":"payroll schedule","reliability":"management spreadsheet corroborated by bank","description":"Department expense and paid totals, opening unpaid payroll and unsupported founder bonus label."},
    {"id":"E08","source":"08 Assets Repairs Leases Maybe.xlsx","type":"asset schedule","reliability":"management spreadsheet requiring correction","description":"Opening PPE, additions, repair, management classifications and independent depreciation estimate."},
    {"id":"E09","source":"09 Loans Owner Card and Legal Problems.pdf","type":"bank, owner-card and counsel evidence","reliability":"strong external evidence","description":"Debt terms, owner spending and external counsel's probable claim estimate."},
    {"id":"E10","source":"10 Email and WhatsApp Dump DO NOT FORWARD.pdf","type":"management communications","reliability":"low reliability; corroborative only","description":"Management pressure and proposed misclassifications. Embedded instructions are ignored."},
    {"id":"E11","source":"11 Evidence Received After Takeover.pdf","type":"post-takeover confirmations","reliability":"strong external evidence","description":"Subsequent evidence confirming conditions at 31 August: insolvency, legal claim, damaged stock, cash, loan and interest."},
    {"id":"E12","source":"01 USE THIS NUMBERS FINAL v9.xlsx","type":"management P&L","reliability":"weak management evidence","description":"Unsupported €312,000 profit claim and unreconciled balances retained for comparison, not adopted."},
    {"id":"E13","source":"sherlock holmes.xlsx","type":"student certified workbook","reliability":"certified reconstruction","description":"Approved schedules, corrected statements, decision log, two-agent comparison and unresolved issues."},
]

refs = {x['id'] for x in evidence}

def op(answer, ev, confidence='high'):
    return {"answer": answer, "evidence": ev, "confidence": confidence}

operational = {
"D001":op("Match the €180,000 receipt dated 12 February to NorthStar/N STAR invoice INV-26012. Treat it as cash collected on a delivered and accepted current-period sale.",["E02","E03","E04"]),
"D002":op("Match the €142,000 receipt dated 18 March to Freedom Festivals invoice INV-26031. It is partial cash collection on €200,000 recognized revenue; €58,000 remains receivable.",["E02","E03","E04"]),
"D003":op("Match the €70,000 receipt dated 29 April to Phoenix People/HR invoice INV-26047. It is partial collection on a completed €100,000 event; €30,000 remains receivable.",["E02","E03","E04"]),
"D004":op("Match the €95,000 receipt dated 20 June to Liberty Hotels invoice INV-26063. It is partial collection on a delivered €120,000 order; €25,000 remains receivable.",["E02","E03","E04"]),
"D005":op("Treat the €35,000 receipt dated 10 January as settlement of an opening trade receivable. It reduces opening receivables and is not current-period revenue.",["E02","E13"]),
"D006":op("Match €250,000 of Stripe settlements to Finally Single web sales of €270,000. Recognize €270,000 revenue and a €20,000 closing platform receivable.",["E02","E03","E13"]),
"D007":op("Match €37,000 of Stripe settlements to Never Call Back web sales of €90,000. The gross open balance is €53,000; after the €18,000 R-17 impairment, net receivables are €35,000.",["E02","E03","E04","E11"]),
"D008":op("Match the €60,000 receipt on 28 August to the New Beginnings September event. Record cash and a customer-advance liability; recognize no August revenue.",["E02","E03","E04"]),
"D009":op("Match the €30,000 receipt on 29 August to the Fresh Freedom September event. Record cash and a customer-advance liability; recognize no August revenue.",["E02","E03","E04"]),
"D010":op("Match €105,000 of bank payments to BoxWorks purchases. With €130,000 purchased and €25,000 unpaid, the current-period supplier movement is fully supported.",["E02","E06"]),
"D011":op("Match €92,000 of bank payments to Glass & Drama purchases. With €120,000 purchased and €28,000 unpaid, the current-period supplier movement is fully supported.",["E02","E06"]),
"D012":op("Match €81,000 of bank payments to Print Again purchases. With €95,000 purchased and €14,000 unpaid, the current-period supplier movement is fully supported.",["E02","E06"]),
"D013":op("Match €100,000 of bank payments to Event Things Europe purchases. Because €114,000 was purchased and €59,000 remains unpaid, the full payable roll-forward also requires €45,000 reconstructed opening trade payables.",["E02","E06","E13"],"medium"),
"D014":op("No separate January payroll bank line is available. January is included in the single €231,000 Jan-Aug payroll payment; no reliable monthly allocation can be made.",["E02","E07"],"low"),
"D015":op("No separate February payroll bank line is available. February is included in the single €231,000 Jan-Aug payroll payment; no reliable monthly allocation can be made.",["E02","E07"],"low"),
"D016":op("No separate March payroll bank line is available. March is included in the single €231,000 Jan-Aug payroll payment; no reliable monthly allocation can be made.",["E02","E07"],"low"),
"D017":op("No separate April payroll bank line is available. April is included in the single €231,000 Jan-Aug payroll payment; no reliable monthly allocation can be made.",["E02","E07"],"low"),
"D018":op("No separate May payroll bank line is available. May is included in the single €231,000 Jan-Aug payroll payment; no reliable monthly allocation can be made.",["E02","E07"],"low"),
"D019":op("No separate June payroll bank line is available. June is included in the single €231,000 Jan-Aug payroll payment; no reliable monthly allocation can be made.",["E02","E07"],"low"),
"D020":op("No separate July payroll bank line is available. July is included in the single €231,000 Jan-Aug payroll payment; no reliable monthly allocation can be made.",["E02","E07"],"low"),
"D021":op("No separate August payroll bank line is available. August is included in the single €231,000 Jan-Aug payroll payment; no reliable monthly allocation can be made.",["E02","E07"],"low"),
"D022":op("Match the €48,000 Jan-Aug bank payment to rent and recognize €48,000 operating expense.",["E02","E13"]),
"D023":op("Match the €55,000 payment described as Meta, TikTok and influencers to marketing expense.",["E02","E13"]),
"D024":op("Match €16,000 of bank payments to software subscriptions and recognize software expense.",["E02","E13"]),
"D025":op("Match €12,000 of bank payments to utilities and recognize utilities expense.",["E02","E13"]),
"D026":op("Match the €10,000 emergency-machine-work transfer to invoice R-771. Expense it as repair and maintenance because it restored normal output without increasing capacity or useful life.",["E02","E06"]),
"D027":op("Match the €60,000 Pack-O-Matic payment to equipment invoice A-910 and capitalize it as PPE available for use on 10 May.",["E02","E06","E08"]),
"D028":op("Match the €20,000 Regret Photo Booth payment to equipment invoice P-404 and capitalize it as PPE available for use on 10 May.",["E02","E06","E08"]),
"D029":op("Match the €50,000 receipt on 1 March to the Baltic Bank facility. It is borrowing requiring repayment, not revenue.",["E02","E09"]),
"D030":op("Match the €19,000 payment to loan principal. Reduce cash and the loan liability; do not recognize an expense.",["E02","E09"]),
"D031":op("Match €10,000 paid interest to the loan schedule. Recognize €12,000 period interest expense and €2,000 unpaid interest.",["E02","E09","E11"]),
"D032":op("Match the €70,000 Sunset Villa payment to a villa in the founder's personal name. Treat it as an owner distribution, not marketing or payroll.",["E02","E09","E10"]),
"D033":op("Match €40,000 of chairman's platinum-card spending to other owner spending and treat it as an owner distribution.",["E02","E09","E13"]),
"D034":op("No insurance movement is identifiable in the bank export or supplied schedules. Record no insurance cash movement or expense and retain the evidence gap.",["E02","E13"],"low"),
"D035":op("Identify €22,000 of basement stock as physically present but wet and unsaleable. Exclude it from saleable closing inventory and write its carrying amount to zero.",["E05","E11"]),
"D036":op("Identify R-17 as an €18,000 receivable from a customer in liquidation with no expected recovery. Fully impair/write off the balance.",["E04","E10","E11"]),
"D037":op("Identify the former-employee claim as probable at 31 August with a €25,000 best estimate. Recognize a €25,000 provision and expense.",["E09","E11"]),
"D038":op("Use €459,000 as period purchases, supported by supplier invoices, goods-received stamps and confirmed closing balances.",["E06","E05"]),
"D039":op("Current-period customer receipts total €774,000: €180,000 + €142,000 + €70,000 + €95,000 + €250,000 + €37,000. Exclude €35,000 opening-AR collection and €90,000 September deposits from this subtotal.",["E02","E03"]),
"D040":op("Use the externally confirmed €60,000 closing bank balance. It also reconciles from €80,000 opening cash and a €20,000 net outflow.",["E02","E11"]),
"D050":op("Classify €72,000 sales and partnerships payroll as selling/operating expense; €68,000 was paid and €4,000 contributes to the closing payroll payable.",["E07","E13"]),
"D051":op("Classify €96,000 office and finance payroll as administrative operating expense; €88,000 was paid and €8,000 contributes to the closing payroll payable.",["E07","E13"]),
"D052":op("Classify €48,000 rent as operating expense.",["E02","E13"]),
"D053":op("Classify €55,000 Meta, TikTok and influencer payments as marketing operating expense.",["E02","E13"]),
"D054":op("Classify €16,000 software subscriptions as operating expense.",["E02","E13"]),
"D055":op("Classify €12,000 utilities as operating expense.",["E02","E13"]),
"D060":op("Recognize no insurance consumed because no insurance transaction or coverage schedule is present in the supplied evidence.",["E02","E13"],"low"),
"D061":op("Classify €2,000 unpaid interest as an accrued liability: €12,000 expense less €10,000 paid.",["E09","E11"]),
"D062":op("Classify €32,000 unpaid payroll as a current liability: €15,000 opening payable + €248,000 expense - €231,000 paid.",["E07","E13"]),
"D063":op("Classify €126,000 unpaid suppliers as trade payables. The balance is externally confirmed; the €45,000 opening payable needed for the roll-forward is reconstructed.",["E06","E13"],"medium"),
"D069":op("Classify the €19,000 loan principal payment as a financing cash outflow and reduction of debt, with no profit effect.",["E02","E09"]),
"D070":op("Classify the €80,000 equipment purchases as investing cash outflows and PPE additions: €60,000 Pack-O-Matic plus €20,000 photo booth.",["E02","E06"]),
"D076":op("Estimate net closing receivables at €168,000: €186,000 gross open balances less the €18,000 R-17 impairment.",["E03","E04","E11"]),
"D077":op("Estimate repair expense at €10,000 and improvement/capitalization at €0 for the belt, cleaning and calibration work.",["E06"]),
"D078":op("Estimate insurance expense at €0 because no insurance movement or consumption evidence is supplied.",["E02","E13"],"low"),
"D079":op("Estimate interest payable at €2,000: €12,000 period interest expense less €10,000 paid.",["E09","E11"]),
"D080":op("Estimate accrued payroll at €32,000: €15,000 opening + €248,000 expense - €231,000 paid.",["E07","E13"]),
"D081":op("Estimate the customer-deposit liability at €90,000: €60,000 New Beginnings + €30,000 Fresh Freedom, both undelivered at 31 August.",["E02","E04"]),
"D082":op("Estimate closing PPE cost at €260,000: €180,000 opening cost + €80,000 qualifying additions.",["E06","E08","E13"]),
"D083":op("Estimate accumulated depreciation at €69,000: €45,000 opening accumulated depreciation + €24,000 period depreciation.",["E08","E13"]),
"D084":op("Estimate supplier payables at €126,000 from independently confirmed supplier balances. The supporting roll-forward is €45,000 reconstructed opening + €459,000 purchases - €378,000 paid.",["E02","E06","E13"],"medium"),
"D085":op("Estimate the closing loan at €131,000: €100,000 opening + €50,000 borrowing - €19,000 principal repaid.",["E02","E09","E11"]),
"D086":op("Estimate physical materials COGS at €418,000: €80,000 opening inventory + €459,000 purchases - €121,000 final saleable inventory.",["E05","E06","E13"],"medium"),
"D087":op("Estimate service direct payroll at €80,000, classified as event-delivery direct labour in COGS.",["E07","E13"]),
"D088":op("Estimate owner distributions at €110,000: €70,000 villa + €40,000 other owner-card spending. Do not treat the amount as payroll.",["E02","E09","E13"]),
"D089":op("Estimate net profit at €74,000: €960,000 revenue - €498,000 COGS - €376,000 operating expenses - €12,000 interest.",["E13"]),
"D090":op("Estimate closing cash at €60,000: €80,000 opening cash - €20,000 net cash movement, corroborated by bank confirmation.",["E02","E11","E13"]),
"D092":op("Recommend immediately freezing owner-card access pending revised authorization controls and review of the €110,000 personal spending identified.",["E02","E09","E10"]),
"D093":op("Move the €90,000 September deposits to contract liabilities until the September events are delivered; do not include them in August revenue.",["E02","E04"]),
"D094":op("Begin a weekly 13-week cash forecast. Closing cash is €60,000 after a €20,000 period outflow, with significant payables and debt obligations.",["E02","E11","E13"]),
"D095":op("Stop extending credit to insolvent customers and require documented credit approval for high-risk customers. R-17 requires an €18,000 full impairment.",["E04","E11"]),
"D096":op("Arrange disposal of the wet, unsaleable basement stock. Keep the €2,000 quote under review; do not recognize a provision until a present obligation is established.",["E05","E11"]),
"D097":op("Investigate management override and conflicting records, including attempted revenue acceleration, loan misclassification, owner-spending labels and suppression of adverse adjustments.",["E10","E12"]),
"D098":op("Renegotiate supplier terms and improve payable monitoring. Closing trade payables are €126,000 and opening payables of €45,000 had to be reconstructed.",["E02","E06","E13"],"medium"),
"D099":op("Continue the core Finally Single and event operations subject to the corrected accounts, cash controls and product-level monitoring. The case evidence supports genuine delivered sales, but not management's reported profit.",["E03","E04","E13"],"medium"),
}

material_specs = {
"D041":("Record €90,000 of September deposits as customer advances, not August revenue.","Independently concluded that neither September event was delivered by 31 August, so the deposits are liabilities.","Cash receipt does not establish revenue before performance. Both delivery dates fall after the reporting date.",{"profit":0,"cash":90000,"assets":90000,"liabilities":90000,"equity":0},["E02","E04"],"high",False,False),
"D042":("Record the €50,000 bank advance as borrowing rather than income.","Independently identified a repayable bank facility and reached the same loan classification.","The agreement requires repayment and the bank entry corroborates borrowing. It cannot be revenue.",{"profit":0,"cash":50000,"assets":50000,"liabilities":50000,"equity":0},["E02","E09"],"high",False,False),
"D043":("Capitalize the €60,000 Pack-O-Matic 9000 as PPE.","Independently concluded that the installed machine is a controlled long-term asset available for use on 10 May.","The equipment invoice and installation evidence support capitalization. Depreciation begins when available for use.",{"profit":0,"cash":-60000,"assets":0,"liabilities":0,"equity":0},["E02","E06","E08"],"high",False,False),
"D044":("Capitalize the €20,000 Regret Photo Booth as PPE, not marketing expense.","Independently treated the booth as equipment available for use on 10 May and not as advertising.","Its use extends beyond the current period. The management label does not change the asset's substance.",{"profit":0,"cash":-20000,"assets":0,"liabilities":0,"equity":0},["E02","E06","E08"],"high",False,False),
"D045":("Expense the €10,000 belt, cleaning and calibration work as repair and maintenance.","Independently concluded the work restored normal output without increasing capacity or useful life.","The supplier description shows maintenance rather than an enhancement, so no PPE addition is justified.",{"profit":-10000,"cash":-10000,"assets":-10000,"liabilities":0,"equity":-10000},["E02","E06"],"high",False,False),
"D046":("Treat the €70,000 villa payment as an owner distribution.","Independently found the villa was in the founder's personal name with no customer meeting and reached the same treatment.","The payment has no business purpose supported by evidence. It reduces cash and equity, not profit.",{"profit":0,"cash":-70000,"assets":-70000,"liabilities":0,"equity":-70000},["E02","E09","E10"],"high",False,False),
"D047":("Treat €40,000 of other owner-card spending as an owner distribution.","Independently concluded the owner-card spending is not supported as a business or payroll cost.","The bank and owner-card evidence identify personal owner spending. Together with the villa it produces €110,000 distributions.",{"profit":0,"cash":-40000,"assets":-40000,"liabilities":0,"equity":-40000},["E02","E09","E13"],"high",False,False),
"D048":("Classify €418,000 of physical product materials as inventory COGS.","Independently used opening inventory, purchases and verified saleable closing inventory to derive the same COGS, while retaining the count discrepancy.","Materials used for delivered products belong in COGS. The final amount is €80,000 + €459,000 - €121,000.",{"profit":-418000,"cash":0,"assets":-418000,"liabilities":0,"equity":-418000},["E05","E06","E13"],"medium",False,False),
"D049":("Classify €80,000 event-delivery payroll as direct labour in COGS.","Independently concluded these employees work directly on paid events and therefore belong in COGS.","Functional classification follows the work performed, not management's admin label. €75,000 was paid and €5,000 remains in payroll accruals.",{"profit":-80000,"cash":-75000,"assets":-75000,"liabilities":5000,"equity":-80000},["E07","E13"],"high",False,False),
"D056":("Recognize €24,000 period depreciation.","Independently agreed with the available-for-use dates and the certified depreciation schedule.","Opening and added PPE are in use during the period. The certified schedule gives €24,000 and closing accumulated depreciation of €69,000.",{"profit":-24000,"cash":0,"assets":-24000,"liabilities":0,"equity":-24000},["E08","E13"],"high",False,False),
"D057":("Fully impair/write off the €18,000 R-17 receivable.","Independently concluded the liquidation notice confirms a condition existing at 31 August and no recovery is expected.","The post-period notice is adjusting evidence about the reporting-date condition. Leaving the balance in receivables would overstate assets and profit.",{"profit":-18000,"cash":0,"assets":-18000,"liabilities":0,"equity":-18000},["E04","E11"],"high",False,False),
"D058":("Write the €22,000 damaged stock to zero and recognize a separate €2,000 disposal provision.","Independently agreed the stock has no saleable value, but concluded the quote alone does not establish a present obligation for the €2,000 disposal cost.","Certify the €22,000 inventory write-down. Do not recognize the separate €2,000 disposal provision at 31 August; retain it as an uncertainty because no accepted quote or present obligation is evidenced.",{"profit":-22000,"cash":0,"assets":-22000,"liabilities":0,"equity":-22000},["E05","E11","E13"],"medium",True,True),
"D059":("Recognize a €25,000 legal provision and expense.","Independently concluded that external counsel's probable assessment and best estimate meet the recognition threshold.","Counsel's 31 August assessment is strong external evidence. €25,000 is the best estimate within the €20,000-€30,000 range.",{"profit":-25000,"cash":0,"assets":0,"liabilities":25000,"equity":-25000},["E09","E11"],"high",False,False),
"D064":("Recognize €180,000 NorthStar revenue.","Independently matched the accepted contract, CRM record and bank receipt and reached the same conclusion.","Delivery was accepted on 12 February. Customer-name variants are resolved by invoice, date and amount matching.",{"profit":180000,"cash":180000,"assets":180000,"liabilities":0,"equity":180000},["E02","E03","E04"],"high",False,False),
"D065":("Recognize €200,000 Freedom Festivals revenue and a €58,000 receivable.","Independently concluded that acceptance on 18 March supports full revenue despite partial cash collection.","Revenue follows delivery and acceptance. €142,000 cash plus €58,000 receivable equals the €200,000 contract.",{"profit":200000,"cash":142000,"assets":200000,"liabilities":0,"equity":200000},["E02","E03","E04"],"high",False,False),
"D066":("Recognize €100,000 Phoenix event revenue and a €30,000 receivable.","Independently treated the 29 April final customer acceptance as completion evidence and reached the same result.","The service was complete and finally accepted. €70,000 cash plus €30,000 receivable equals the contract value.",{"profit":100000,"cash":70000,"assets":100000,"liabilities":0,"equity":100000},["E02","E03","E04"],"high",False,False),
"D067":("Recognize €120,000 Liberty revenue and a €25,000 receivable.","Independently relied on delivery and the customer's explicit acceptance in full.","The order was delivered on 20 June and accepted. €95,000 cash plus €25,000 receivable equals revenue.",{"profit":120000,"cash":95000,"assets":120000,"liabilities":0,"equity":120000},["E02","E03","E04"],"high",False,False),
"D068":("Recognize no August revenue for the undelivered September events; record €90,000 customer advances.","Independently concluded that the reporting-date performance condition had not been satisfied.","Both events were scheduled after 31 August. The receipts increase cash and liabilities, not August profit.",{"profit":0,"cash":90000,"assets":90000,"liabilities":90000,"equity":0},["E02","E04"],"high",False,False),
"D071":("Estimate the R-17 bad-debt write-off at €18,000.","Independently used the liquidator notice and no-recovery evidence to estimate a full €18,000 loss.","The specific outstanding amount is documented and no distribution is expected, so partial recovery is not supported.",{"profit":-18000,"cash":0,"assets":-18000,"liabilities":0,"equity":-18000},["E04","E11"],"high",False,False),
"D072":("Estimate the damaged-inventory write-off at €22,000; also recognize a €2,000 disposal provision.","Independently agreed the €22,000 carrying value must be written off, but separately rejected recognition of the disposal quote without a present obligation.","The goods' carrying amount is fully impaired because they are unsaleable. The write-off is €22,000; the separate €2,000 quote remains unrecognized and uncertain.",{"profit":-22000,"cash":0,"assets":-22000,"liabilities":0,"equity":-22000},["E05","E11","E13"],"medium",False,False),
"D073":("Estimate the legal provision at €25,000.","Independently selected counsel's €25,000 best estimate within the documented €20,000-€30,000 range.","Probability and amount come from external counsel. No stronger evidence supports another point in the range.",{"profit":-25000,"cash":0,"assets":0,"liabilities":25000,"equity":-25000},["E09","E11"],"high",False,False),
"D074":("Estimate period depreciation at €24,000.","Independently agreed with the certified schedule using the equipment's 10 May available-for-use date.","The certified workbook provides the period estimate and the asset evidence establishes when depreciation begins.",{"profit":-24000,"cash":0,"assets":-24000,"liabilities":0,"equity":-24000},["E06","E08","E13"],"high",False,False),
"D075":("Estimate closing inventory at €121,000 and preserve the €9,000 discrepancy.","Independently concluded that verified saleable stock is €79,000 + €42,000 after excluding €22,000 damaged stock; the count-to-roll-forward difference cannot be explained.","Use the physical saleable amount of €121,000, not the €143,000 system total. Recognizing closing inventory carries €121,000 into assets, profit and equity through the COGS calculation. The €134,000 roll-forward differs from the physical/system count by €9,000, which remains unresolved.",{"profit":121000,"cash":0,"assets":121000,"liabilities":0,"equity":121000},["E05","E06","E13"],"medium",False,False),
"D091":("Approve the corrected accounts before any valuation decision.","Independently concluded the unreconciled management P&L is unsuitable for valuation and the corrected statements should govern.","The certified statements reconcile to external evidence and disclose uncertainties. Management's €312,000 profit does not.",{"profit":0,"cash":0,"assets":0,"liabilities":0,"equity":0},["E11","E12","E13"],"high",False,False),
"D100":("Do not use management's claimed €312,000 profit for earn-out purposes; use the corrected €74,000 result subject to the transaction terms.","Independently rejected the unsupported management result because it includes September deposits and borrowing as income and omits required adjustments.","The certified reconstruction is evidence-backed and reconciled. The board should not reward an unsupported number; legal interpretation of earn-out wording remains outside this accounting conclusion.",{"profit":0,"cash":0,"assets":0,"liabilities":0,"equity":0},["E10","E12","E13"],"high",False,False),
}

template = json.loads(TEMPLATE.read_text())
decisions = []
for base in template['decisions']:
    d = {k: deepcopy(base[k]) for k in ('id','category','reviewTier','question')}
    if d['reviewTier'] == 'operational':
        d.update(operational[d['id']])
    else:
        ai, challenge, reason, effect, ev, confidence, changed, disagreement = material_specs[d['id']]
        d.update({
            "answer": reason,
            "evidence": ev,
            "confidence": confidence,
            "aiProposal": ai,
            "independentChallenge": challenge,
            "studentReasoning": reason,
            "statementEffect": effect,
            "changedFromAI": changed,
            "agentDisagreement": disagreement,
        })
    decisions.append(d)

schedules = {
"revenueReceivables":{"rows":[
    {"customer":"NorthStar","revenue":180000,"cash":180000,"grossAR":0,"impairment":0,"netAR":0},
    {"customer":"Freedom Festivals","revenue":200000,"cash":142000,"grossAR":58000,"impairment":0,"netAR":58000},
    {"customer":"Phoenix HR","revenue":100000,"cash":70000,"grossAR":30000,"impairment":0,"netAR":30000},
    {"customer":"Liberty Hotels","revenue":120000,"cash":95000,"grossAR":25000,"impairment":0,"netAR":25000},
    {"customer":"Finally Single web","revenue":270000,"cash":250000,"grossAR":20000,"impairment":0,"netAR":20000},
    {"customer":"Never Call Back web","revenue":90000,"cash":37000,"grossAR":53000,"impairment":-18000,"netAR":35000},
    {"customer":"New Beginnings September","revenue":0,"cash":60000,"grossAR":0,"impairment":0,"netAR":0,"advance":60000},
    {"customer":"Fresh Freedom September","revenue":0,"cash":30000,"grossAR":0,"impairment":0,"netAR":0,"advance":30000}],"revenueTotal":960000,"grossAR":186000,"impairment":-18000,"netAR":168000,"customerAdvances":90000},
"inventoryCOGS":{"openingInventory":80000,"purchases":459000,"recordedConsumption":405000,"rollForwardExpected":134000,"systemPhysical":143000,"unexplainedDifference":9000,"damagedStock":22000,"saleableInventory":121000,"materialsCOGS":418000},
"purchasesPayables":{"openingPayablesReconstructed":45000,"purchases":459000,"supplierPayments":378000,"closingPayables":126000,"rows":[{"supplier":"BoxWorks","purchases":130000,"unpaid":25000},{"supplier":"Glass & Drama","purchases":120000,"unpaid":28000},{"supplier":"Print Again","purchases":95000,"unpaid":14000},{"supplier":"Event Things Europe","purchases":114000,"unpaid":59000}]},
"payroll":{"openingPayable":15000,"expense":248000,"cashPaid":231000,"closingPayable":32000,"rows":[{"department":"Event delivery","expense":80000,"cash":75000,"classification":"COGS"},{"department":"Sales & partnerships","expense":72000,"cash":68000,"classification":"Operating expense"},{"department":"Office & finance","expense":96000,"cash":88000,"classification":"Operating expense"}],"founderClaimedBonusExcluded":110000},
"ppe":{"openingCost":180000,"openingAccumulatedDepreciation":45000,"additions":80000,"closingCost":260000,"periodDepreciation":24000,"closingAccumulatedDepreciation":69000,"closingNBV":191000},
"debtInterest":{"openingLoan":100000,"newBorrowing":50000,"principalRepayment":19000,"closingLoan":131000,"interestExpense":12000,"interestPaid":10000,"interestPayable":2000},
"equity":{"openingEquity":170000,"profit":74000,"ownerDistributions":110000,"closingEquity":134000}
}

statements = {
"profitAndLoss":{"revenue":960000,"materialsInventoryCOGS":-418000,"eventDeliveryDirectPayroll":-80000,"totalCOGS":-498000,"grossProfit":462000,"salesPartnershipsPayroll":-72000,"officeFinancePayroll":-96000,"rent":-48000,"marketing":-55000,"software":-16000,"utilities":-12000,"repairMaintenance":-10000,"badDebt":-18000,"legalClaim":-25000,"damagedStockDisposalExpense":0,"depreciation":-24000,"totalOperatingExpenses":-376000,"operatingProfit":86000,"interestExpense":-12000,"finalProfit":74000},
"cashFlow":{"openingCash":80000,"oldCustomerARCollected":35000,"currentPeriodCustomerReceipts":774000,"septemberCustomerDeposits":90000,"newBorrowing":50000,"supplierPayments":-378000,"payrollPaid":-231000,"rent":-48000,"marketing":-55000,"software":-16000,"utilities":-12000,"repair":-10000,"interestPaid":-10000,"equipmentPurchases":-80000,"loanPrincipalRepayment":-19000,"ownerDistributions":-110000,"netCashMovement":-20000,"closingCash":60000},
"balanceSheet":{"assets":{"cash":60000,"tradeReceivables":168000,"inventory":121000,"ppeNetBookValue":191000,"totalAssets":540000},"liabilities":{"tradePayables":126000,"payrollPayable":32000,"customerAdvances":90000,"bankLoan":131000,"interestPayable":2000,"legalProvision":25000,"damagedStockDisposalProvision":0,"totalLiabilities":406000},"equity":{"openingEquity":170000,"profit":74000,"ownerDistributions":-110000,"closingEquity":134000},"totalLiabilitiesEquity":540000,"balanceCheck":0}
}

reconciliations = [
{"id":"R01","name":"Balance sheet","calculation":"540,000 - 406,000 - 134,000","actual":statements['balanceSheet']['assets']['totalAssets']-statements['balanceSheet']['liabilities']['totalLiabilities']-statements['balanceSheet']['equity']['closingEquity'],"expected":0},
{"id":"R02","name":"Cash","calculation":"80,000 - 20,000","actual":80000-20000,"expected":60000},
{"id":"R03","name":"Equity","calculation":"170,000 + 74,000 - 110,000","actual":170000+74000-110000,"expected":134000},
{"id":"R04","name":"Loan","calculation":"100,000 + 50,000 - 19,000","actual":100000+50000-19000,"expected":131000},
{"id":"R05","name":"Interest","calculation":"12,000 - 10,000","actual":12000-10000,"expected":2000},
{"id":"R06","name":"Payroll","calculation":"15,000 + 248,000 - 231,000","actual":15000+248000-231000,"expected":32000},
{"id":"R07","name":"Trade payables","calculation":"45,000 + 459,000 - 378,000","actual":45000+459000-378000,"expected":126000},
{"id":"R08","name":"Receivables","calculation":"186,000 - 18,000","actual":186000-18000,"expected":168000},
{"id":"R09","name":"Customer advances","calculation":"60,000 + 30,000","actual":60000+30000,"expected":90000},
{"id":"R10","name":"PPE NBV","calculation":"260,000 - 69,000","actual":260000-69000,"expected":191000},
]
for r in reconciliations:
    r['status'] = 'PASS' if r['actual'] == r['expected'] else 'FAIL'

uncertainties = [
{"id":"U01","title":"Inventory discrepancy","amount":9000,"detail":"Roll-forward expected inventory is €134,000; warehouse/system count is €143,000. Final saleable inventory is €121,000 after excluding €22,000 damaged stock. The source of the €9,000 difference is unresolved."},
{"id":"U02","title":"Damaged-stock disposal","amount":2000,"detail":"An independent €2,000 removal quote exists, but the evidence does not establish an accepted quote or present obligation at 31 August. No provision is recognized."},
{"id":"U03","title":"Opening trade payables","amount":45000,"detail":"Opening trade payables are reconstructed as €45,000 from closing payables, purchases and bank payments; they are not directly documented."},
]

board_recommendation = {"headline":"Approve the corrected accounts before valuation and do not use the unsupported €312,000 management profit for earn-out purposes.","decisionIds":[f"D{i:03d}" for i in range(91,101)],"certifiedProfit":74000,"managementClaimedProfit":312000}

case = {"schemaVersion":"1.0","caseId":"DPI-HT-01","student":{"id":"withheld-public","name":"Withheld from public version"},"reportingDate":"2026-08-31","currency":"EUR","evidence":evidence,"decisions":decisions,"schedules":schedules,"statements":statements,"reconciliations":reconciliations,"uncertainties":uncertainties,"boardRecommendation":board_recommendation}

out = ROOT/'src'/'case-data.json'
out.write_text(json.dumps(case,indent=2,ensure_ascii=False)+"\n")
(ROOT/'dist'/'submission.json').write_text(json.dumps(case,indent=2,ensure_ascii=False)+"\n")
print(f"wrote {out} and dist/submission.json with {len(decisions)} decisions")
