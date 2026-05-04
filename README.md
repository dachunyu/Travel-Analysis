# 🌏 旅游景点分析与AI路线推荐系统 / Travel Analysis & AI Route Recommendation System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## プロジェクト概要 / Project Overview

中国と日本の観光スポット情報を収集・分析し、AIを活用した旅行ルート推薦システムです。DeepSeek大規模言語モデルを統合し、ユーザーの予算・日程・季節に基づいてパーソナライズされた旅行プランを提供します。

A tourism analysis and AI-powered route recommendation system for China and Japan attractions. Integrates DeepSeek LLM to provide personalized travel plans based on user budget, schedule, and season.

## 主要機能 / Key Features

### 1. データ収集 / Data Collection
-**Google Maps API**: 日本の観光スポット671件を収集
-**高德地図API**: 中国49都市の観光スポット4,887件を収集
-**総データ量**: 5,558件の観光スポット情報

### 2. データ分析 / Data Analysis
- 評価スコア分布分析
- 都市別人気スポットランキング
- チケット価格帯分析
- 地理的分布の可視化
- レビュー数ランキング

### 3. Webシステム / Web System
- ユーザー登録・ログイン機能
- 観光スポット検索・フィルタリング
- レスポンシブデザイン（Bootstrap 5）
- SimpleUIによる管理画面の美化

### 4. AI旅行ルート推薦 / AI Route Recommendation
- **DeepSeek大規模言語モデル統合**
- ユーザー入力に基づくパーソナライズ推薦
  - 目的地都市
  - 旅行季節
  - 行程日数
  - 予算
- 百度地図による経路可視化

## 技術スタック / Tech Stack

### バックエンド / Backend
- **フレームワーク**: Django 4.2
- **データベース**: MySQL
- **データ処理**: Pandas
- **API統合**: 
  - Google Maps Places API
  - 高德地図API
  - DeepSeek API (OpenAI SDK)

### フロントエンド / Frontend
- **UI Framework**: Bootstrap 5
- **アイコン**: Font Awesome 6
- **テンプレートエンジン**: Django Templates

### データ可視化 / Data Visualization
- ECharts 5（評価分布・地域別ランキングなど）
- 百度地図API

## インストール / Installation

### 1. リポジトリのクローン / Clone Repository
```bash
git clone https://github.com/yourusername/travelanalysis.git
cd travelanalysis
```

### 2. 仮想環境の作成 / Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 依存関係のインストール / Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. データベース設定 / Database Setup
```bash
# MySQLデータベースを作成
mysql -u root -p
CREATE DATABASE travelAnalysis CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;

# マイグレーション実行
python manage.py migrate
```

### 5. 設定ファイル / Configuration
```bash
# config_template.pyをコピーしてconfig.pyを作成
cp config_template.py config.py

# config.pyを編集して、以下を設定：
# - データベース接続情報
# - API キー（DeepSeek, Google Maps, 高德地図）
```

### 6. データインポート / Import Data
```bash
cd data
python import_data.py      # 中国の観光スポットデータ
python import_jp_data.py   # 日本の観光スポットデータ
```

### 7. サーバー起動 / Start Server
```bash
python manage.py runserver
```

ブラウザで http://127.0.0.1:8000/ にアクセス

## データセット / Dataset

| 項目 | 詳細 |
|------|------|
| **総データ数** | 5,558件 |
| **中国観光スポット** | 4,887件（49都市） |
| **日本観光スポット** | 671件（35都市） |
| **データ項目** | 名称、住所、評価、経緯度、価格、レビュー数など |

## プロジェクトの特徴 / Project Highlights

1. **大規模データ収集**: 複数のAPIを活用し、5,000件以上の観光スポット情報を収集
2. **AI統合**: DeepSeek大規模言語モデルによる知的な旅行プラン生成
3. **多次元分析**: Pandasを用いた8つの分析視点からのデータ洞察
4. **実用的なWebシステム**: ユーザー認証、検索、フィルタリング機能を備えた完全なWebアプリケーション
5. **国際対応**: 中国と日本の観光スポットをカバー

## スクリーンショット / Screenshots

<img width="2974" height="1996" alt="1630071777890087_ pic" src="https://github.com/user-attachments/assets/811be619-d8db-49c7-b5b2-a709d26f10e1" />

<img width="2974" height="1996" alt="1630081777890087_ pic" src="https://github.com/user-attachments/assets/68b1e157-fb18-4045-acad-066378d678e9" />

<img width="2974" height="1996" alt="1630091777890087_ pic" src="https://github.com/user-attachments/assets/018617cd-b150-47c2-bcb4-26a84e292f8c" />

<img width="2960" height="1990" alt="1630101777890087_ pic" src="https://github.com/user-attachments/assets/194c47c4-5829-4f9e-b2c2-aed974c4f5c9" />

<img width="2974" height="1996" alt="1630111777890088_ pic" src="https://github.com/user-attachments/assets/145e575f-76ef-492c-bf5c-20b72b96da12" />

<img width="2974" height="1996" alt="1630121777890088_ pic" src="https://github.com/user-attachments/assets/b8dacf0c-7dc8-4873-a4fb-7125a855505a" />

<img width="2974" height="1996" alt="1630131777890088_ pic" src="https://github.com/user-attachments/assets/84bde1d9-b8ef-45e7-a437-d39b9809f889" />

<img width="2974" height="1996" alt="1630151777890088_ pic" src="https://github.com/user-attachments/assets/a51e8f78-38d5-4254-9c1c-e44e6ed360fa" />



## 今後の改善 / Future Improvements

- [ ] データ可視化ダッシュボードの強化
- [ ] 百度地図による経路表示機能の実装
- [ ] ユーザーレビュー機能の追加
- [ ] お気に入り機能の実装
- [ ] 多言語対応（日本語・英語）
- [ ] モバイルアプリ版の開発

## 開発者 / Developer

**董宸妤 (Dong Chenyu)**
- Python開発経験: 1年
- 専門分野: データ分析、AI応用、Web開発

## 謝辞 / Acknowledgments

- Google Maps Places API
- 高德地図API
- DeepSeek AI
- Django Community
