import os
import discord
import requests
from discord.ext import commands
from decouple import config

# Initialize bot intent configurations
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Fetch target endpoint values from root environment vars
API_BASE_URL = "http://127.0.0.1:8000/api/status/"

@bot.event
async def on_ready():
    print("=" * 60)
    print(f"DISCORD INTERFACE BOT ONLINE | Authenticated as: {bot.user.name}")
    print(f"   Listening on endpoint connection: {API_BASE_URL}")
    print("=" * 60)

@bot.command(name='status')
async def system_status(ctx):
    """Fetches full office metrics and device profiles."""
    try:
        response = requests.get(API_BASE_URL)
        if response.status_code != 200:
            await ctx.send("Error context: Failed communicating with the central Django gateway architecture.")
            return
            
        data = response.json()
        
        embed = discord.Embed(
            title="Smart Office System Status", 
            color=discord.Color.blue()
        )
        embed.add_field(name="Total Power Draw", value=f"{data['total_power_w']} W ({data['total_power_kw']} kW)", inline=True)
        embed.add_field(name="Appliances Active", value=f"🟢 {data['active_devices_count']} / {data['total_devices_count']}", inline=True)
        
        # Room breakdown compilation strings
        for room in data['rooms']:
            device_lines = []
            for d in room['devices']:
                icon = "🌀" if d['device_type'] == "FAN" else "💡"
                status_icon = "🟢" if d['status'] == "ON" else "🔴"
                device_lines.append(f"{icon} {d['name']}: {status_icon} **{d['status']}**")
            
            embed.add_field(
                name=f"{room['name']} ({room['total_power']}W Active)", 
                value="\n".join(device_lines) if device_lines else "No devices tracked.", 
                inline=False
            )
            
        # Append alert state diagnostics if triggered
        if data['alerts']:
            alert_text = "\n".join([f"**{a['severity']}**: {a['message']}" for a in data['alerts']])
            embed.add_field(name="System Active Risks", value=alert_text, inline=False)
            
        await ctx.send(embed=embed)
        
    except Exception as e:
        await ctx.send(f"Internal interface tracking communication failure: {str(e)}")

@bot.command(name='usage')
async def total_usage(ctx):
    """Fast shortcut command displaying basic consumption diagnostics."""
    try:
        response = requests.get(API_BASE_URL)
        data = response.json()
        msg = (
            f"**Current Combined Power Metrics:**\n"
            f"──► Total Wattage Draw: `{data['total_power_w']} W`\n"
            f"──► System Active Load Count: `{data['active_devices_count']} Devices Active`"
        )
        await ctx.send(msg)
    except Exception as e:
        await ctx.send(f"System error gathering usage metrics: {str(e)}")

@bot.command(name='bothelp')
async def custom_help(ctx):
    """Lists available commands for the interface panel."""
    help_text = (
        "**IoT Office Automation Interface Core Commands:**\n"
        "`!status` - Retreives a complete matrix profile of all rooms, loads, and power states.\n"
        "`!usage`  - Provides brief snapshot calculations of cumulative wattage data streams.\n"
        "`!bothelp` - Displays this operational control catalog map."
    )
    await ctx.send(help_text)

# Token invocation bootstrap call
if __name__ == "__main__":
    TOKEN = config("DISCORD_BOT_TOKEN", default="")