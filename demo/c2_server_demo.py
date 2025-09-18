#!/usr/bin/env python3
"""
C2 Server Demo Script
Demonstrates the capabilities of the Advanced C2 Server
"""

import requests
import json
import time

def demo_c2_server():
    """Demo the C2 server capabilities"""
    
    print("🚀 C2 Server Demo")
    print("=" * 50)
    
    # Check server health
    print("\n1. Checking Server Health...")
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            health_data = response.json()
            print(f"   ✅ Server Status: {health_data['status']}")
            print(f"   📦 Version: {health_data['version']}")
            print(f"   🎯 Simulation Mode: {health_data['simulation']}")
        else:
            print(f"   ❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Health check error: {e}")
    
    # Check dashboard data
    print("\n2. Fetching Dashboard Data...")
    try:
        response = requests.get("http://localhost:8000/api/dashboard")
        if response.status_code == 200:
            dashboard_data = response.json()
            print(f"   📊 Active Sessions: {dashboard_data.get('sessions', 0)}")
            print(f"   🎯 Active Listeners: {dashboard_data.get('listeners', 0)}")
            print(f"   💣 Generated Payloads: {dashboard_data.get('payloads', 0)}")
            print(f"   🔥 Available Exploits: {dashboard_data.get('exploits', 0)}")
        else:
            print(f"   ❌ Dashboard API failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Dashboard API error: {e}")
    
    # Check devices/agents
    print("\n3. Checking Connected Agents...")
    try:
        response = requests.get("http://localhost:8000/api/devices")
        if response.status_code == 200:
            devices = response.json()
            print(f"   🤖 Connected Agents: {len(devices)}")
            for device in devices[:3]:  # Show first 3 devices
                print(f"      - {device.get('name', 'Unknown')} ({device.get('device_type', 'Unknown')})")
        else:
            print(f"   ❌ Devices API failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Devices API error: {e}")
    
    # Check exploits
    print("\n4. Available Exploits...")
    try:
        response = requests.get("http://localhost:8000/api/exploits")
        if response.status_code == 200:
            exploits = response.json()
            print(f"   💀 Total Exploits: {len(exploits)}")
            for exploit in exploits[:3]:  # Show first 3 exploits
                print(f"      - {exploit.get('name', 'Unknown')} ({exploit.get('type', 'Unknown')})")
        else:
            print(f"   ❌ Exploits API failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Exploits API error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 C2 Server Demo Complete!")
    print("\n📊 Key Features Demonstrated:")
    print("   • Real-time agent monitoring")
    print("   • Advanced payload generation")
    print("   • GSM/SS7 network exploitation")
    print("   • 0-click exploit framework")
    print("   • Web-based dashboard interface")
    print("   • Secure command & control")

if __name__ == "__main__":
    demo_c2_server()
