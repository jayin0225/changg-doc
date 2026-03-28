import { NextResponse } from 'next/server';

// Prerender.io Token - 替换为你的真实 Token
const PRERENDER_TOKEN = 'YOUR_TOKEN_HERE';

// 需要预渲染的爬虫 User-Agent
const CRAWLER_USER_AGENTS = [
  'googlebot',
  'bingbot',
  'baiduspider',
  'slurp',
  'duckduckbot',
  'facebookexternalhit',
  'twitterbot',
  'linkedinbot',
  'whatsapp',
  'telegrambot'
];

export function middleware(request) {
  const userAgent = request.headers.get('user-agent') || '';
  const isCrawler = CRAWLER_USER_AGENTS.some(ua => 
    userAgent.toLowerCase().includes(ua)
  );

  // 如果是爬虫，重定向到 prerender.io
  if (isCrawler) {
    const url = new URL(request.url);
    const prerenderUrl = `https://service.prerender.io/${url.href}`;
    
    const response = NextResponse.rewrite(prerenderUrl);
    response.headers.set('X-Prerender-Token', PRERENDER_TOKEN);
    
    return response;
  }

  return NextResponse.next();
}

export const config = {
  matcher: '/:path*'
};
