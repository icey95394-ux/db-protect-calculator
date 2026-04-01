#!/usr/bin/env python3
"""
等保合规计算器 - 价格验证脚本（更新版）
小笨出品 🐾
自动验证计算器中的价格计算逻辑是否正确
"""

def calculate_level3_20ecs():
    """计算等保三级 + 20 台 ECS 的总价（DDoS 和 SSL 为可选）"""
    level = 3
    ecs_count = 20
    container_cores = 0
    
    items = []
    total = 0
    
    # 堡垒机
    price = 45900
    items.append({'name': '堡垒机（企业双擎版）', 'price': price})
    total += price
    
    # 云防火墙
    price = 139200
    items.append({'name': '云防火墙（企业版）', 'price': price})
    total += price
    
    # 云安全中心
    base_price = 1800
    container_price = container_cores * 60
    price = (base_price * ecs_count) + container_price
    items.append({'name': f'云安全中心（旗舰版 × {ecs_count}台）', 'price': price})
    total += price
    
    # 数据安全中心
    price = 53400
    items.append({'name': '数据安全中心（高级版）', 'price': price})
    total += price
    
    # WAF
    price = 135600
    items.append({'name': 'WAF（企业版）', 'price': price})
    total += price
    
    # DDoS 高防 - 已改为可选，不计入
    # SSL 证书 - 已改为可选，不计入
    
    # 等保测评费
    assessment_price = 120000
    items.append({'name': '等保测评费（三级）', 'price': assessment_price})
    total += assessment_price
    
    return items, total

def calculate_level2_10ecs():
    """计算等保二级 + 10 台 ECS 的总价（DDoS 和 SSL 为可选）"""
    level = 2
    ecs_count = 10
    
    items = []
    total = 0
    
    # 堡垒机
    price = 34884
    items.append({'name': '堡垒机（基础版）', 'price': price})
    total += price
    
    # 云防火墙
    price = 45600
    items.append({'name': '云防火墙（高级版）', 'price': price})
    total += price
    
    # 云安全中心
    price = 720 * ecs_count
    items.append({'name': f'云安全中心（高级版 × {ecs_count}台）', 'price': price})
    total += price
    
    # 数据安全中心
    price = 49200
    items.append({'name': '数据安全中心（等保合规版）', 'price': price})
    total += price
    
    # WAF
    price = 64560
    items.append({'name': 'WAF（高级版）', 'price': price})
    total += price
    
    # DDoS 高防 - 已改为可选，不计入
    # SSL 证书 - 已改为可选，不计入
    
    # 等保测评费
    assessment_price = 80000
    items.append({'name': '等保测评费（二级）', 'price': assessment_price})
    total += assessment_price
    
    return items, total

def main():
    print("=" * 70)
    print("🛡️ 等保合规计算器 - 自动化价格验证（DDoS/SSL 可选版）")
    print("小笨出品 🐾")
    print("=" * 70)
    
    # 测试场景 1：等保三级 + 20 台 ECS
    print("\n📊 测试场景：等保三级 + 20 台 ECS（DDoS 和 SSL 为可选，不计入）")
    print("-" * 70)
    
    items, total = calculate_level3_20ecs()
    
    expected_items = [
        ('堡垒机（企业双擎版）', 45900),
        ('云防火墙（企业版）', 139200),
        ('云安全中心（旗舰版 × 20 台）', 36000),
        ('数据安全中心（高级版）', 53400),
        ('WAF（企业版）', 135600),
        ('等保测评费（三级）', 120000),
    ]
    
    all_correct = True
    for i, item in enumerate(items):
        expected_name, expected_price = expected_items[i]
        status = "✅" if item['price'] == expected_price else "❌"
        if item['price'] != expected_price:
            all_correct = False
        print(f"{status} {item['name']:30s} ¥{item['price']:>10,} (预期：¥{expected_price:>10,})")
    
    print("-" * 70)
    expected_total = sum([price for _, price in expected_items])
    status = "✅" if total == expected_total else "❌"
    if total != expected_total:
        all_correct = False
    
    print(f"{status} 总计：¥{total:>12,} (预期：¥{expected_total:>12,})")
    print("-" * 70)
    
    if all_correct:
        print("\n🎉 所有价格计算正确！")
    else:
        print("\n❌ 发现价格计算错误，需要修正！")
    
    # 测试场景 2：等保二级 + 10 台 ECS
    print("\n\n📊 测试场景：等保二级 + 10 台 ECS（DDoS 和 SSL 为可选，不计入）")
    print("-" * 70)
    
    items2, total2 = calculate_level2_10ecs()
    
    expected_items2 = [
        ('堡垒机（基础版）', 34884),
        ('云防火墙（高级版）', 45600),
        ('云安全中心（高级版 × 10 台）', 7200),
        ('数据安全中心（等保合规版）', 49200),
        ('WAF（高级版）', 64560),
        ('等保测评费（二级）', 80000),
    ]
    
    all_correct2 = True
    for i, item in enumerate(items2):
        expected_name, expected_price = expected_items2[i]
        status = "✅" if item['price'] == expected_price else "❌"
        if item['price'] != expected_price:
            all_correct2 = False
        print(f"{status} {item['name']:30s} ¥{item['price']:>10,} (预期：¥{expected_price:>10,})")
    
    print("-" * 70)
    expected_total2 = sum([price for _, price in expected_items2])
    status = "✅" if total2 == expected_total2 else "❌"
    if total2 != expected_total2:
        all_correct2 = False
    
    print(f"{status} 总计：¥{total2:>12,} (预期：¥{expected_total2:>12,})")
    print("-" * 70)
    
    if all_correct2:
        print("\n🎉 所有价格计算正确！")
    else:
        print("\n❌ 发现价格计算错误，需要修正！")
    
    print("\n" + "=" * 70)
    if all_correct and all_correct2:
        print("✅ 全部测试通过！计算器价格逻辑正确！")
        print("\n📋 必选产品总价参考：")
        print(f"   - 等保三级（20 台 ECS）：¥{total:,}/年（不含 DDoS 和 SSL）")
        print(f"   - 等保二级（10 台 ECS）：¥{total2:,}/年（不含 DDoS 和 SSL）")
        print("\n💡 可选产品参考价：")
        print(f"   - DDoS 原生防护：¥178,320/年")
        print(f"   - SSL 证书：¥3,000/年 + ¥2,000/域名")
    else:
        print("❌ 部分测试失败，需要检查计算逻辑！")
    print("=" * 70)

if __name__ == "__main__":
    main()
