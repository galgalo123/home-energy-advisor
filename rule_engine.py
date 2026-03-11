# rule_engine.py — Kenya Home Energy-Saving Advisor

def get_recommendations(profile):
    recommendations = []
    bill = profile['monthly_bill_ksh']
    size = profile['home_size']
    bulbs = profile['bulb_type']
    has_ac = profile['has_ac']
    appliance_age = profile['appliance_age']
    cooking_fuel = profile['cooking_fuel']
    has_geyser = profile['has_geyser']

    # ── ELECTRICITY BILL RULES (KSh) ────────────────────────────────────────
    if bill > 10000:
        recommendations.append({
            "tip": "Your KPLC bill is critically high. Request a free energy audit from Kenya Power by calling 97771 or visiting kplc.co.ke.",
            "category": "Billing",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Ask Kenya Power about a Time-of-Use tariff — running heavy appliances at night (off-peak) can significantly reduce your bill.",
            "category": "Billing",
            "priority": "🔴 High"
        })
    elif bill > 5000:
        recommendations.append({
            "tip": "Your bill is above the average Kenyan household. Track which appliances run the longest each day to find the biggest drains.",
            "category": "Billing",
            "priority": "🟡 Medium"
        })
        recommendations.append({
            "tip": "Unplug devices like TVs, phone chargers and microwaves when not in use — standby power can account for up to 10% of your KPLC bill.",
            "category": "Billing",
            "priority": "🟡 Medium"
        })
    elif bill <= 2000:
        recommendations.append({
            "tip": "Your bill is low — great job! Keep monitoring monthly to maintain your efficiency, especially as KPLC tariffs continue to change.",
            "category": "Billing",
            "priority": "🟢 Low"
        })

    # ── LIGHTING RULES ──────────────────────────────────────────────────────
    if bulbs == 'incandescent':
        recommendations.append({
            "tip": "Switch to LED bulbs immediately — they use 75% less electricity and last much longer. A single LED bulb pays for itself within months on your KPLC bill.",
            "category": "Lighting",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Install motion sensors in low-traffic areas like hallways, toilets and outside — widely available at hardware shops across Kenya.",
            "category": "Lighting",
            "priority": "🟡 Medium"
        })
    elif bulbs == 'fluorescent':
        recommendations.append({
            "tip": "Consider upgrading from fluorescent to LED — LEDs are now cheaper and more efficient, and widely available at hardware shops across Kenya.",
            "category": "Lighting",
            "priority": "🟡 Medium"
        })
    elif bulbs == 'led':
        recommendations.append({
            "tip": "Great choice using LED bulbs! Add dimmer switches or timers to save even more on lighting costs.",
            "category": "Lighting",
            "priority": "🟢 Low"
        })

    # ── COOKING FUEL RULES ──────────────────────────────────────────────────
    if cooking_fuel == 'charcoal':
        recommendations.append({
            "tip": "Charcoal is expensive long-term and harmful to health. Transitioning to LPG is cheaper per meal and cleaner — the government has zero-rated LPG VAT to make it more affordable.",
            "category": "Cooking",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Visit one of KPLC's eCooking hubs in Nairobi, Mombasa, Nakuru or Kisumu to see Electric Pressure Cookers (EPCs) in action — they use a quarter of the energy of a charcoal stove.",
            "category": "Cooking",
            "priority": "🟡 Medium"
        })
    elif cooking_fuel == 'kerosene':
        recommendations.append({
            "tip": "Kerosene is being phased out in Kenya by 2030. Switch to LPG now — it is safer, cleaner, and costs less per meal in the long run.",
            "category": "Cooking",
            "priority": "🔴 High"
        })
    elif cooking_fuel == 'firewood':
        recommendations.append({
            "tip": "Firewood contributes to deforestation and indoor air pollution. Transition to LPG or an Improved Cookstove (ICS) as a first step — both are widely available across Kenya.",
            "category": "Cooking",
            "priority": "🔴 High"
        })
    elif cooking_fuel == 'lpg':
        recommendations.append({
            "tip": "Good choice using LPG! Consider an Electric Pressure Cooker (EPC) as a supplement — it uses only 0.21 kWh per meal, making it the most energy-efficient cooking option in Kenya.",
            "category": "Cooking",
            "priority": "🟢 Low"
        })
    elif cooking_fuel == 'electric':
        recommendations.append({
            "tip": "Electric cooking is clean and efficient. Run your electric cooker during off-peak hours to take advantage of lower KPLC rates if you are on a Time-of-Use tariff.",
            "category": "Cooking",
            "priority": "🟢 Low"
        })

    # ── WATER HEATING (GEYSER) RULES ────────────────────────────────────────
    if has_geyser:
        recommendations.append({
            "tip": "Your electric water heater (geyser) is likely your single biggest electricity cost. Install a solar water heater — Kenya's high year-round solar irradiation means ROI within 2–3 years.",
            "category": "Water Heating",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Set your geyser thermostat to 55°C instead of the default 70°C — you will not notice the difference but your KPLC bill will.",
            "category": "Water Heating",
            "priority": "🟡 Medium"
        })
        recommendations.append({
            "tip": "Install a geyser timer to only heat water in the mornings and evenings when you need it, rather than keeping it on all day.",
            "category": "Water Heating",
            "priority": "🟡 Medium"
        })
    else:
        recommendations.append({
            "tip": "Using a gas or solar water heater is a great energy choice. If you ever upgrade, consider an instant solar geyser for the best efficiency.",
            "category": "Water Heating",
            "priority": "🟢 Low"
        })

    # ── AIR CONDITIONING RULES ──────────────────────────────────────────────
    if has_ac and size == 'large':
        recommendations.append({
            "tip": "Install a programmable thermostat — set it to 24–26°C and avoid cooling empty rooms. Each degree lower increases energy use by approximately 6%.",
            "category": "Cooling",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Seal gaps around doors and windows — air leaks force your AC to work harder. Use weather stripping from any Nairobi hardware shop.",
            "category": "Cooling",
            "priority": "🟡 Medium"
        })
    elif has_ac and size == 'medium':
        recommendations.append({
            "tip": "Clean your AC filter monthly — dirty filters make the unit work harder and draw more electricity from KPLC.",
            "category": "Cooling",
            "priority": "🟡 Medium"
        })
    elif not has_ac:
        recommendations.append({
            "tip": "No AC detected — use blackout curtains, ceiling fans, and cross-ventilation (open windows at opposite ends of your house at night) to naturally cool your home.",
            "category": "Cooling",
            "priority": "🟢 Low"
        })

    # ── APPLIANCE RULES ─────────────────────────────────────────────────────
    if appliance_age == 'old':
        recommendations.append({
            "tip": "Appliances older than 10 years consume up to 50% more electricity. Prioritise replacing your refrigerator and washing machine first — look for energy-efficient models at Nairobi appliance retailers.",
            "category": "Appliances",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Defrost your old refrigerator regularly — ice buildup makes the compressor work harder and draws more power from the grid.",
            "category": "Appliances",
            "priority": "🟡 Medium"
        })
    elif appliance_age == 'medium':
        recommendations.append({
            "tip": "Service your appliances annually — clean refrigerator coils and check door seals to maintain efficiency.",
            "category": "Appliances",
            "priority": "🟡 Medium"
        })
        recommendations.append({
            "tip": "Wash clothes in cold water — works just as well for most laundry and uses significantly less electricity.",
            "category": "Appliances",
            "priority": "🟡 Medium"
        })
    elif appliance_age == 'new':
        recommendations.append({
            "tip": "New appliances are efficient — maximise savings by running heavy appliances like washing machines during off-peak hours.",
            "category": "Appliances",
            "priority": "🟢 Low"
        })

    # ── HOME SIZE RULES ─────────────────────────────────────────────────────
    if size == 'large':
        recommendations.append({
            "tip": "Large homes in Kenya lose significant heat through uninsulated roofs. Consider reflective roofing sheets or ceiling insulation to reduce cooling costs.",
            "category": "Insulation",
            "priority": "🟡 Medium"
        })
        recommendations.append({
            "tip": "Kenya has high solar irradiation year-round — large homes have more roof space and higher bills, making the ROI on solar panels faster. Consult a KEBS-certified solar installer.",
            "category": "Renewable Energy",
            "priority": "🟡 Medium"
        })
    elif size == 'small':
        recommendations.append({
            "tip": "Small homes heat and cool quickly — use timers on your heating or cooling appliances so they only run when needed.",
            "category": "Insulation",
            "priority": "🟢 Low"
        })

    # ── COMBINED MULTI-FACTOR RULES ─────────────────────────────────────────
    if bill > 7000 and appliance_age == 'old' and bulbs == 'incandescent':
        recommendations.append({
            "tip": "⚠️ URGENT: You have three major energy drains — high KPLC bill, old appliances, and inefficient bulbs. Addressing all three could cut your bill by 40–60%.",
            "category": "Overall",
            "priority": "🔴 High"
        })

    if bill > 5000 and has_geyser and cooking_fuel in ['charcoal', 'kerosene', 'firewood']:
        recommendations.append({
            "tip": "⚠️ Your high bill combined with an electric geyser and dirty cooking fuel is a costly combination. Switching to a solar water heater and LPG cooking could save you KSh 3,000–5,000 per month.",
            "category": "Overall",
            "priority": "🔴 High"
        })

    if not recommendations:
        recommendations.append({
            "tip": "Your home appears to be running efficiently for a Kenyan household. Keep monitoring your KPLC monthly statements to stay on track.",
            "category": "Overall",
            "priority": "🟢 Low"
        })

    return recommendations