# rule_engine.py

def get_recommendations(profile):
    recommendations = []
    bill = profile['monthly_bill']
    size = profile['home_size']
    bulbs = profile['bulb_type']
    has_ac = profile['has_ac']
    appliance_age = profile['appliance_age']

    # ── ELECTRICITY BILL RULES ──────────────────────────────────────────
    if bill > 300:
        recommendations.append({
            "tip": "Your electricity bill is critically high. Consider a full home energy audit immediately.",
            "category": "Billing",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Contact your electricity provider about a Time-of-Use plan — run heavy appliances at night when rates are lower.",
            "category": "Billing",
            "priority": "🔴 High"
        })
    elif bill > 150:
        recommendations.append({
            "tip": "Your bill is above average. Track which appliances run the longest each day.",
            "category": "Billing",
            "priority": "🟡 Medium"
        })
        recommendations.append({
            "tip": "Unplug devices when not in use — standby power can account for up to 10% of your bill.",
            "category": "Billing",
            "priority": "🟡 Medium"
        })
    elif bill <= 80:
        recommendations.append({
            "tip": "Your bill is low — great job! Keep monitoring monthly to maintain efficiency.",
            "category": "Billing",
            "priority": "🟢 Low"
        })

    # ── LIGHTING RULES ──────────────────────────────────────────────────
    if bulbs == 'incandescent':
        recommendations.append({
            "tip": "Switch to LED bulbs immediately — they use 75% less energy and last 25x longer than incandescent bulbs.",
            "category": "Lighting",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Install motion sensors in low-traffic areas like hallways and bathrooms to avoid lights being left on.",
            "category": "Lighting",
            "priority": "🟡 Medium"
        })
    elif bulbs == 'fluorescent':
        recommendations.append({
            "tip": "Consider upgrading from fluorescent to LED — LEDs are more efficient and contain no mercury.",
            "category": "Lighting",
            "priority": "🟡 Medium"
        })
    elif bulbs == 'led':
        recommendations.append({
            "tip": "Great choice using LED bulbs! Add dimmer switches to save even more on lighting costs.",
            "category": "Lighting",
            "priority": "🟢 Low"
        })

    # ── AIR CONDITIONING RULES ──────────────────────────────────────────
    if has_ac and size == 'large':
        recommendations.append({
            "tip": "Install a smart/programmable thermostat — automatically adjusting temperature by 7–10°F when away can save up to 10% annually.",
            "category": "Cooling",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Seal gaps around doors and windows — air leaks force your AC to work harder and waste energy.",
            "category": "Cooling",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Use ceiling fans alongside your AC — they make rooms feel cooler, letting you raise the thermostat by 4°F without discomfort.",
            "category": "Cooling",
            "priority": "🟡 Medium"
        })
    elif has_ac and size == 'medium':
        recommendations.append({
            "tip": "Set your AC to 24–26°C (75–78°F) — each degree lower increases energy use by about 6%.",
            "category": "Cooling",
            "priority": "🟡 Medium"
        })
        recommendations.append({
            "tip": "Clean your AC filter monthly — dirty filters make the unit work harder and consume more power.",
            "category": "Cooling",
            "priority": "🟡 Medium"
        })
    elif has_ac and size == 'small':
        recommendations.append({
            "tip": "For a small home, a portable or window AC unit may be more efficient than central air.",
            "category": "Cooling",
            "priority": "🟢 Low"
        })
    elif not has_ac:
        recommendations.append({
            "tip": "No AC detected — use blackout curtains and strategic ventilation (open windows at night) to naturally cool your home.",
            "category": "Cooling",
            "priority": "🟢 Low"
        })

    # ── APPLIANCE RULES ─────────────────────────────────────────────────
    if appliance_age == 'old':
        recommendations.append({
            "tip": "Old appliances (10+ years) can use up to 50% more energy than modern equivalents — prioritise replacing your refrigerator and washing machine first.",
            "category": "Appliances",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "When replacing appliances, always look for the Energy Star label — they meet strict efficiency guidelines.",
            "category": "Appliances",
            "priority": "🔴 High"
        })
        recommendations.append({
            "tip": "Defrost your old refrigerator regularly — ice buildup makes it work harder and use more electricity.",
            "category": "Appliances",
            "priority": "🟡 Medium"
        })
    elif appliance_age == 'medium':
        recommendations.append({
            "tip": "Your appliances are mid-age — service them annually (clean coils, check seals) to maintain efficiency.",
            "category": "Appliances",
            "priority": "🟡 Medium"
        })
        recommendations.append({
            "tip": "Wash clothes in cold water — it works just as well for most loads and uses far less energy.",
            "category": "Appliances",
            "priority": "🟡 Medium"
        })
    elif appliance_age == 'new':
        recommendations.append({
            "tip": "New appliances are efficient — maximise savings by running them during off-peak hours (evenings/weekends).",
            "category": "Appliances",
            "priority": "🟢 Low"
        })

    # ── HOME SIZE RULES ─────────────────────────────────────────────────
    if size == 'large':
        recommendations.append({
            "tip": "Large homes lose significant heat/cool air through the roof — ensure your attic has proper insulation (R-38 or higher).",
            "category": "Insulation",
            "priority": "🟡 Medium"
        })
        recommendations.append({
            "tip": "Consider installing solar panels — large homes have more roof space and higher bills, making solar ROI much faster.",
            "category": "Renewable Energy",
            "priority": "🟡 Medium"
        })
    elif size == 'small':
        recommendations.append({
            "tip": "Small homes heat and cool quickly — use a timer on your heating/cooling so it only runs when needed.",
            "category": "Insulation",
            "priority": "🟢 Low"
        })

    # ── COMBINED / MULTI-FACTOR RULES ───────────────────────────────────
    if bill > 200 and appliance_age == 'old' and bulbs == 'incandescent':
        recommendations.append({
            "tip": "⚠️ URGENT: You have three major energy drains — high bill, old appliances, and inefficient bulbs. Addressing all three could cut your bill by 40–60%.",
            "category": "Overall",
            "priority": "🔴 High"
        })

    if bill > 150 and has_ac and size == 'large' and appliance_age == 'old':
        recommendations.append({
            "tip": "⚠️ Your combination of high bill, large home, AC, and old appliances suggests a full energy retrofit would pay for itself within 2–3 years.",
            "category": "Overall",
            "priority": "🔴 High"
        })

    if not recommendations:
        recommendations.append({
            "tip": "Your home appears to be running efficiently. Keep monitoring your monthly usage to stay on track.",
            "category": "Overall",
            "priority": "🟢 Low"
        })

    return recommendations