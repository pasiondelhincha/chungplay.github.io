#! /usr/bin/python3
banner = r'''
#EXTINF:-1 group-title="💡 | Play On-Air" tvg-logo="https://fptplay.vn/images/logo-2.png" tvg-chno="0" ,FPT Giới Thiệu
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://livecdn.fptplay.net/hda4/f-channel.stream/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="💡 | Play On-Air" tvg-logo="https://static.fptplay.net/static/img/share/channels/icon_channel_pladio_163947930147.png" ,Pladio Show - FPT Radio
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda3/pladio_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="💡 | Play On-Air" tvg-logo="https://blog-cloudflare-com-assets.storage.googleapis.com/2019/07/cf-logo-social-media.png" ,Cloudflare TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://cloudflare.tv/hls/live.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtv1hd_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv1hd.png" tvg-id="vtv1hd" tvg-chno="1" ,VTV1 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/vtv1hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtv2_2000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv2hd.png" tvg-id="vtv2hd" tvg-chno="2" ,VTV2 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/vtv2_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtv3hd_1500.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv3hd.png" tvg-id="vtv3hd" tvg-chno="3" ,VTV3 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/vtv3hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtv4_2000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv4hd.png" tvg-id="vtv4hd" tvg-chno="4" ,VTV4 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/vtv4_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtv5hd_1500.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv5hd.png" tvg-id="vtv5hd" tvg-chno="5" ,VTV5 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda2/vtv5hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv5tn.png" tvg-id="vtv5tn" ,VTV5 Tây Nguyên
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://mutixx5hq1liv.akamaized.net/vtv5tn/vtv5tn@720p.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv5tnb.png" tvg-id="vtv5tnb" ,VTV5 Tây Nguyên HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://mutixx5hq1liv.akamaized.net/vtv5tnb/vtv5tnb@720p.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtv6hd_1500.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv6hd.png" tvg-id="vtv5hd" tvg-chno="6" ,VTV6 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/vtv6hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtv7hd_1500.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv8hd.png" tvg-id="vtv7hd" tvg-chno="7" ,VTV7 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda2/vtv8hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtv8hd_1500.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv8hd.png" tvg-id="vtv8hd" tvg-chno="8" ,VTV8 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda2/vtv8hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtv9hd_1500.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🇻🇳 | Kênh VTV - FPT" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv9hd.png" tvg-id="vtv9hd" tvg-chno="9" ,VTV9 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda2/vtv9_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - VTVGiaiTri.VN" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv1hd.png" tvg-id="vtv1hd" ,VTV1 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://drfamaga5qliv.vcdn.cloud/vtv01/vtv01@1080p.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - VTVGiaiTri.VN" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv2hd.png" tvg-id="vtv2hd" ,VTV2 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://drfamaga5qliv.vcdn.cloud/vtv02/vtv02@1080p.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - VTVGiaiTri.VN" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv3hd.png" tvg-id="vtv3hd" ,VTV3 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://drfamaga5qliv.vcdn.cloud/vtv03/vtv03@1080p.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - VTVGiaiTri.VN" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv4hd.png" tvg-id="vtv4hd" ,VTV4 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://drfamaga5qliv.vcdn.cloud/vtv04/vtv04@1080p.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - VTVGiaiTri.VN" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv5hd.png" tvg-id="vtv5hd" ,VTV5 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://drfamaga5qliv.vcdn.cloud/vtv05/vtv05@1080p.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - VTVGiaiTri.VN" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv6hd.png" tvg-id="vtv6hd" ,VTV6 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://drfamaga5qliv.vcdn.cloud/vtv06/vtv06@1080p.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - VTVGiaiTri.VN" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv7hd.png" tvg-id="vtv7hd" ,VTV7 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://drfamaga5qliv.vcdn.cloud/vtv07/vtv07@1080p.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - VTVGiaiTri.VN" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv8hd.png" tvg-id="vtv8hd" ,VTV8 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://drfamaga5qliv.vcdn.cloud/vtv08/vtv08@1080p.m3u8
#EXTINF:-1 group-title="🇻🇳 | Kênh VTV - VTVGiaiTri.VN" tvg-logo="https://chungmaster.github.io/logo/vtv/vtv9hd.png" tvg-id="vtv9hd" ,VTV9 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://drfamaga5qliv.vcdn.cloud/vtv09/vtv09@1080p.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 1 - Vie GIẢITRÍ" tvg-logo="https://imgstatic.vtvcab.vn/logos/GIAITRI_TV_HD_M.png" tvg-id="vtvcab1hd" ,VTVCab1 - Vie GIẢITRÍ SD
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab1/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-name="VTVCab 1 - Vie GIẢITRÍ" tvg-logo="https://imgstatic.vtvcab.vn/logos/GIAITRI_TV_HD_M.png" group-title="🏷️ | Kênh VTVCab" tvg-id="vtvcab1hd" ,VTVCab1 - Vie GIẢITRÍ HD
http://gg.gg/VieGIAITRIHD
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 2 - Kênh Phim truyện Việt Nam" tvg-logo="https://mytv.com.vn/upload/channel/phpMg6DY5_613966915655d.png" tvg-id="vtvcab2hd" ,VTVCab2 - ON Phim Việt
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 3 - Kênh thể thao" tvg-logo="https://mytv.com.vn/upload/channel/phpLhy8IQ_613966bf6fda5.png" tvg-id="vtvcab3hd" ,VTVCab3 - On Sports
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab3/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 4 HD - Kênh phim truyện và giải trí đa phương tiện" tvg-logo="https://chungmaster.github.io/logo/vtvcab/VTVcab_4.png" tvg-id="vtvcab4hd" ,VTVCab4 - LOVE TV
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab4/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 5 - Kênh phim truyện và giải trí tổng hợp" tvg-logo="https://imgstatic.vtvcab.vn/logos/E_CHANNEL_M.png" tvg-id="vtvcab5hd" ,VTVCab5 - E-CHANNEL
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab5/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 6 - Kênh thể thao giải trí và thông tin kinh tế" tvg-logo="https://chungmaster.github.io/logo/vtvcab/ON-Sports-Plus.png" tvg-id="vtvcab6hd" ,VTVCab6 - ON Sports + SD
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab6/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 6 HD - Kênh thể thao giải trí và thông tin kinh tế" tvg-logo="https://chungmaster.github.io/logo/vtvcab/ON-Sports-Plus.png" tvg-id="vtvcab3hd" ,VTVCab6 - On Sports + HD 
http://gg.gg/OnSportHD
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 7 - Kênh Sức khỏe và Cuộc sống" tvg-logo="https://chungmaster.github.io/logo/vtvcab/VTVCab_7.png" tvg-id="vtvcab7hd" ,VTVCab7 - Sức khỏe và Cuộc sống
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab7/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 8 - Kênh thiếu nhi BiBi" tvg-logo="https://mytv.com.vn/upload/channel/102.png" tvg-id="vtvcab8hd" ,VTVCab8 - BIBI
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab8/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 9 - Kênh thiếu nhi BiBi" tvg-logo="https://mytv.com.vn/upload/channel/195.png" tvg-id="vtvcab9hd" ,VTVCab9 - InfoTV
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab9/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 10 - Kênh phim truyện" tvg-logo="https://mytv.com.vn/upload/channel/phpHCeMwp_613966db69f11.png" tvg-id="vtvcab10hd" ,VTVCab10 - ON Cine
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab10/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 11 - Kênh Mua sắm" tvg-logo="https://shop-media.vgsshop.vn/pub/media/logo/stores/7/gsshop-logo.png" tvg-id="" ,VTVCab11 - GS SHOP (HTVC VGS SHOP Home Shopping)
https://e2.endpoint.cdn.sctvonline.vn/hls/htvcvgs/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 12 - Kênh thời trang, phong cách sống" tvg-logo="https://mytv.com.vn/upload/channel/103.png" tvg-id="vtvcab12hd" ,VTVCab12 - Style TV
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab12/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 13 - Kênh Mua sắm" tvg-logo="https://vtvhyundai.vn/resource/img/logo_og.png" tvg-id="" ,VTVCab13 - VTV Hyundai Home Shopping
https://livecdn.fptplay.net/sdb/vtvhyundai_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 15 - Kênh Âm nhạc" tvg-logo="https://chungmaster.github.io/logo/vtvcab/VTVcab_15.png" tvg-id="vtvcab15hd" ,VTVCab15
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab15/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 16 HD - Kênh thể thao (điển hình về bóng đá)" tvg-logo="https://chungmaster.github.io/logo/vtvcab/VTVCab_16_HD.png" tvg-id="vtvcab16hd" ,VTVCab16 - ON Football HD
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab16/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 17 - Kênh giải trí dành cho giới trẻ" tvg-logo="https://chungmaster.github.io/logo/vtvcab/VTVcab_17.png" tvg-id="vtvcab17hd" ,VTVCab 17 - Yeah1TV
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab17/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 19 - Vie DRAMAS" tvg-logo="https://imgstatic.vtvcab.vn/logos/D_DRAMAS_HD_M.png" tvg-id="vtvcab19hd" ,VTVCab19 - Vie DRAMAS SD
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab19/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 19 - Vie DRAMAS" tvg-logo="https://imgstatic.vtvcab.vn/logos/D_DRAMAS_HD_M.png" tvg-id="vtvcab19hd" ,VTVCab19 - Vie DRAMAS HD
http://gg.gg/VieDRAMASHD
#EXTINF:-1 group-title="🏷️ | Kênh VTVCab"  tvg-name="VTVCab 20 - Kênh giải trí dành cho phụ nữ và gia đình" tvg-logo="https://mytv.com.vn/upload/channel/132.png" tvg-id="vtvcab20hd" ,VTVCab20 - VFamily
https://e3.endpoint.cdn.sctvonline.vn/hls/vtvcab20/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV1 HD - Kênh Hài" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv1hd.png" tvg-id="sctv1hd" ,SCTV1 HD - Hài
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv1/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV2 HD - Kênh NetStars" tvg-logo="https://chungmaster.github.io/logo/sctv/netstars.png" tvg-id="sctv2hd" ,SCTV2 HD - NetStars
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv2/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV2 HD - Kênh NetStars" tvg-logo="https://chungmaster.github.io/logo/sctv/netstars.png" tvg-id="sctv2hd" ,NetStars HD - TV24VN
http://gg.gg/sctv2sd_tv24
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV3 HD - Kênh thiếu nhi" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv3.png" tvg-id="sctv3hd" ,SCTV3 HD - SEE TV
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv3/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV3 HD - Kênh Giải Trí Tổng Hợp" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv4.png" tvg-id="sctv4hd" ,SCTV4 - Giải Trí Tổng Hợp
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv4/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV5 - Kênh mua sắm" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv5.png" tvg-id="sctv5hd" ,SCTV5 - SCJ TV Shopping
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv5/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV6 - Kênh Truyền hình giải trí thế hệ mới" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv6.png" tvg-id="sctv6hd" ,SCTV6
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv6/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/film360_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh SCTV" tvg-name="SCTV6 HD - Kênh Phim FILM360 " tvg-logo="https://chungmaster.github.io/logo/sctv/fim_360.png" tvg-id="sctv6hd" ,SCTV6 HD - FIM360 HD
https://livecdn.fptplay.net/hda3/film360_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV7 - Kênh Sân khấu văn nghệ tổng hợp" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv7.png" tvg-id="sctv7_hd" ,SCTV7 - SHOW TV
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv7/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV8 - Kênh VITV Kinh Tế" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv8.png" tvg-id="sctv8hd" ,SCTV8 - VITV Kinh Tế
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv8/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV9 HD - Kênh Phim Châu Á" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv9hd.png" tvg-id="sctv9hd" ,SCTV9 HD - Phim Châu Á & TVB
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv9/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV10 - Kênh mua sắm thuộc Home Shopping Việt Nam" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv10.png" tvg-id="sctv10hd" ,SCTV10 - VTV Hyundai Home Shopping
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv10/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV11 HD - Kênh Văn Hoá Nghệ Thuật" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv11hd.png" tvg-id="sctv11hd" ,SCTV11 HD - TV STAR
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv11/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV12 HD -Kênh Du Lịch Khám Phá" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv12hd.png" tvg-id="sctv12hd" ,SCTV12 HD - Du Lịch & Khám Phá
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv12/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV12 HD -Kênh Du Lịch Khám Phá" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv12hd.png" tvg-id="sctv12hd" ,SCTV12 HD - TV24VN
http://gg.gg/sctv12_tv24
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV13 HD -Kênh Phụ nữ & Gia đình" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv13.png" tvg-id="sctv13hd" ,SCTV13 - Lady TV
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv13/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV14 HD - Kênh Phim Việt" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv14hd.png" tvg-id="sctv14hd" ,SCTV 14 HD - Phim Việt
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv14/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV15 HD - Kênh Ssport 2" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv15.png" tvg-id="sctv15hd" ,SCTV15 HD - Ssport 2
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv15/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV16 HD - Kênh Phim Nước Ngoài Đặc Sắc" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv16.png" tvg-id="sctv16hd" ,SCTV16 HD - Phim Nước Ngoài Đặc Sắc
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv16/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV17 HD - Kênh Thể Thao Ssport" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv17.png" tvg-id="sctv17hd" ,SCTV17 HD - Ssport
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv17/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV18 - Kênh dành cho thanh thiếu niên" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv18.png" tvg-id="sctv18hd" ,SCTV18 - Kênh 18
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv18/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV18 - Kênh dành cho thanh thiếu niên" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv18.png" tvg-id="sctv18hd" ,SCTV18 - TV24VN
http://gg.gg/sctv18_tv24
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV19 - Kênh dành cho teen" tvg-logo="https://chungmaster.github.io/logo/sctv/tchannel.png" tvg-id="sctv19hd" ,SCTV19 - Channel T
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv19/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV20 - Kênh nhạc bolero và nhạc trẻ" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv20.png" tvg-id="sctv20hd" ,SCTV20 - Ca nhạc tổng hợp
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv20/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV Phim Tổng Hợp HD" tvg-logo="https://chungmaster.github.io/logo/sctv/sctvpth.png" tvg-id="sctvhdpth" ,SCTV Phim Tổng Hợp
https://e1.endpoint.cdn.sctvonline.vn/hls/sctvphimtonghop/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV21 HD - Kênh Việt Nam Ký Ức" tvg-logo="https://chungmaster.github.io/logo/sctv/vietnamkyuc.png" tvg-id="sctv21hd" ,SCTV21 HD - Việt Nam Ký Ức
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv21/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV22 - Kênh SSport 1" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv22.png" tvg-id="sctv22hd" ,SCTV22 - Ssport 1
https://e1.endpoint.cdn.sctvonline.vn/hls/sctv22/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="SCTV22 - Kênh SSport 1" tvg-logo="https://chungmaster.github.io/logo/sctv/sctv22.png" tvg-id="sctv22hd" ,SCTV22 - TV24VN
http://gg.gg/sctv22_tv24
#EXTINF:-1 group-title="🏷️ | Kênh SCTV" tvg-name="BTV5 - Kênh SSport 3" tvg-logo="https://chungmaster.github.io/logo/sctv/BTV5.png" tvg-id="btv5hd" ,BTV5  - Ssport 3
https://e2.endpoint.cdn.sctvonline.vn/hls/btv5/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc1_1500.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC1 HD" tvg-logo="https://mytv.com.vn/upload/channel/75.png" tvg-id="vtc1hd" ,VTC1 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/vtc1_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc2_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC2 HD" tvg-logo="https://mytv.com.vn/upload/channel/21.png" tvg-id="vtc2" ,VTC2
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/vtc2_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc3_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC3 HD" tvg-logo="https://mytv.com.vn/upload/channel/83.png" tvg-id="vtc3hd" ,VTC3 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/vtc3hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc4_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC4 HD" tvg-logo="https://mytv.com.vn/upload/channel/134.png" tvg-id="vtc4hd" ,VTC4 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda2/vtc4_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc5_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-id="vtc5hd" tvg-name="VTC5 HD" tvg-logo="https://mytv.com.vn/upload/channel/187.png" ,VTC5 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/vtc5_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc6_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC6 HD" tvg-logo="https://mytv.com.vn/upload/channel/23.png" tvg-id="vtc6hd" , VTC6 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/vtc6_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc7_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC7 HD" tvg-logo="https://mytv.com.vn/upload/channel/188.png" tvg-id="vtc7hd" , VTC7 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/todaytv_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc8_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC8 HD" tvg-logo="https://mytv.com.vn/upload/channel/164.png" tvg-id="vtc8",VTC8 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/vtc8_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc9_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC9 HD" tvg-logo="https://mytv.com.vn/upload/channel/189.png" tvg-id="vtc9hd" ,VTC9 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/vtc9_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc10_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC10 HD" tvg-logo="https://mytv.com.vn/upload/channel/116.png" tvg-id="vtc10hd" , VTC10 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/vtc10_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc11_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC11 HD" tvg-logo="https://mytv.com.vn/upload/channel/26.png" tvg-id="vtc11", VTC11 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/vtc11_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc12_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC12 HD" tvg-logo="https://mytv.com.vn/upload/channel/phpWgYcFl_5e1d3209b5e25.png" tvg-id="vtc12" , VTC12 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/vtc12_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc13_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC13 HD" tvg-logo="https://mytv.com.vn/upload/channel/78.png" tvg-id="vtc13hd" ,VTC13 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/vtc13_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh VTC - FPT" tvg-id="vtc13hd" tvg-logo="https://portal.vtc.gov.vn/site/img/vtc4k_thumbnail.jpg" ,VTC13 HD 4K
http://vcdn1.vtc.gov.vn:1935/m_4k/smil:4k.smil/playlist.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc14_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC14 HD" tvg-logo="https://mytv.com.vn/upload/channel/207.png" tvg-id="vtc14hd" ,VTC14 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/vtc14_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vtc16_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh VTC - FPT" tvg-name="VTC16 HD" tvg-logo="https://mytv.com.vn/upload/channel/206.png" tvg-id="vtc16" ,VTC16 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/vtc16_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="hitv" tvg-logo="http://imageidc1.tv360.vn/image1/2020_09_23/1600823412691/61627b84a612_640_360.png" group-title="📼 | Kênh Hanoicab" ,Hanoicab 1 - HiTV
https://live2cdn.todayplus.com.vn/sdb/smil:hitv.smil/chunklist_b1596000.m3u8
#EXTINF:-1 tvg-id="youtv" tvg-logo="http://imageidc1.tv360.vn/image1/2020_09_23/1600823396313/7b474bf7bbce_640_360.png" group-title="📼 | Kênh Hanoicab" ,Hanoicab 2 - YouTV
https://livecdn.fptplay.net/sdb/youtv_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="antg" tvg-logo="https://chungmaster.github.io/logo/anninhthegioi.png" group-title="📼 | Kênh Hanoicab" ,Hanoicab 3 - An Ninh Thế Giới
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://e2.endpoint.cdn.sctvonline.vn/hls/antg/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 tvg-id="antg" tvg-logo="https://images.careerbuilder.vn/employer_folders/lot2/85022/134225logoscjdai.png" group-title="📼 | Kênh Hanoicab" ,Hanoicab 5 - SCJ TV Shopping
https://e3.endpoint.cdn.sctvonline.vn/hls/hanoicab5/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/boxmovie.png" tvg-id="boxmovie1" , BOX Movie¹
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://e4.endpoint.cdn.sctvonline.vn/hls/boxmovie1/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/hollywood.png" tvg-id="hollywoodclassics" , Hollywood Classics
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://e4.endpoint.cdn.sctvonline.vn/hls/hollywood/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/inthebox.png"  tvg-id="inthebox" , In The Box
http://gg.gg/inthebox_vthanh
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/boxhits.png"  tvg-id="boxhits" , Box Hits
http://gg.gg/boxhits_vthanh
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/man.png"  tvg-id="man" , MAN
http://gg.gg/man_vthanh
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/musicbox.png" tvg-id="musicbox" , Music Box - FPT 
https://livecdn.fptplay.net/hda3/music_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/musicbox.png" tvg-id="musicbox" , Music Box - NETHub
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://e4.endpoint.cdn.sctvonline.vn/hls/boxmusic/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/woman.png" tvg-id="woman" ,Woman
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://e4.endpoint.cdn.sctvonline.vn/hls/woman/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/planetearth.png" tvg-id="planetearthhd" ,Planet Earth
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://e4.endpoint.cdn.sctvonline.vn/hls/planetearth/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/happykids.png" tvg-id="happykids" ,Happy Kids
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://e4.endpoint.cdn.sctvonline.vn/hls/happykid/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="📦 | Kênh INTHEBOX"  tvg-logo="https://chungmaster.github.io/logo/inthebox/drfit.png" tvg-id="drfithd" ,Dr.Fit
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://e4.endpoint.cdn.sctvonline.vn/hls/drfit/sd2/index.m3u8|Referer=http://sctvonline.vn/
#EXTINF:-1 group-title="🏷️ | Kênh HTV" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/07/16/185783-505482-HTV1.png" tvg-id="htv1" ,HTV1
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/htv1_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTV" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/904719-HTV2HD.png" tvg-id="htv2hd" ,HTV2 HD - HTVC 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTV2-HD-1080p/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTV" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/904719-HTV2HD.png" tvg-id="htv2hd" ,HTV2 HD - FPT
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/htv2hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTV" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/750643-HTV3.png" tvg-id="htv3" ,HTV3 - DreamsTV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTV3-SD-480p/chunks.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTV" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/08/14/359584-htv-key-web.png" tvg-id="htvkey" ,HTV Key
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/htv4_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTV" tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/07/16/928755-665121-HTV7HD.png" tvg-id="htv7hd" ,HTV7 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/htv7hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTV" tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/07/16/422430-665121-HTV9HD.png" tvg-id="htv9hd",HTV9 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/htv9hd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTV" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/07/16/546898-111250-HTVTT.png" tvg-id="htvthethaohd" ,HTV Thể Thao
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda3/htvcthethao_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTV" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/402721-HTVCoop.png" tvg-id="htvc_coop" ,HTV CO.OP
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVCOOP-SD-ABR/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTVC" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/504279-ThuanViet.png" tvg-id="htvcthuanviet" ,HTVC Thuần Việt SD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-THUANVIET-HD-1080p/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTVC" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/136820-ThuanVietHD1.png" tvg-id="htvcthuanviethd" ,HTVC Thuần Việt HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-THUANVIETHD-HD-1080p/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTVC" tvg-logo="http://htvc.vn/uploads/editor/images/Ca%20nhac-01.png" tvg-id="htvccanhachd" ,HTVC Ca Nhạc
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-CANHAC-HD-1080p/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTVC" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/591916-pHIM.png" tvg-id="htvcphimhd" ,HTVC Phim HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-PHIM-HD-1080p/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTVC" tvg-logo="https://img.hplus.com.vn/355x200/poster/2018/06/05/143922-pn.png" tvg-id="htvcphunuhd" ,HTVC Phụ Nữ
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-PHUNU-HD-1080p/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTVC" tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/06/05/866192-Gia-Dinh.png" tvg-id="htvcgiadinhhd" ,HTVC Gia Đình
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-GIADINH-HD-1080p/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTVC" tvg-logo="http://htvc.vn/uploads/channel/2015/02/12/9681507-logo-htvc-dulic.png" tvg-id="htvcdulichhd" ,HTVC Du Lịch & Cuộc Sống
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-DULICH-HD-1080p/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTVC" tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/08/02/451568-logo_htvc_shopping.png" ,HTVC VGS Shop
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HOMESHOPPING-SD-ABR/HTV-ABR/HOMESHOPPING-SD-720p/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh HTVC" tvg-logo="https://chungmaster.github.io/logo/htvc+.png" tvg-id="htvcplushd" ,HTVC + HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/HTVC-PLUS-HD-1080p/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh THỜI SỰ & CHÍNH LUẬN"  tvg-logo="https://mytv.com.vn/upload/channel/35.png" tvg-id="antvhd" ,ANTV HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda2/anninhtv_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh THỜI SỰ & CHÍNH LUẬN" tvg-logo="https://mytv.com.vn/upload/channel/127.png" tvg-id="qpvnhd" ,QPVN
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/quocphongvnhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh THỜI SỰ & CHÍNH LUẬN " tvg-logo="https://mytv.com.vn/upload/channel/128.png" tvg-id="nhandan" ,NHÂN DÂN HD
https://video.nhandan.thienvietjsc.net/live/nhandan720/chunklist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh THỜI SỰ & CHÍNH LUẬN" tvg-logo="https://mytv.com.vn/upload/channel/133.png" tvg-id="ttxvnhd" ,VNEWS - Truyền hình TTXVN
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda2/ttxvn_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh THỜI SỰ & CHÍNH LUẬN" tvg-logo="https://mytv.com.vn/upload/channel/71.png" tvg-id="quochoi" ,QUỐC HỘI
http://113.164.225.140:1935/live/quochoitvlive.stream/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh THỜI SỰ & CHÍNH LUẬN" tvg-logo="https://static.mediacdn.vn/vovTV/web_images/logovov02112020_nobg.png" tvg-id="vovtvhd" ,VOV TV
http://cdn.vovtv.mediatech.vn/vovlive/tv1live.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh THỜI SỰ & CHÍNH LUẬN" tvg-logo="https://chungmaster.github.io/logo/netviet.png" tvg-id="vtc10hd" ,NETVIET TV
http://gg.gg/kenhnetviet
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source=" https://tshift.fptplay.net/dvr/vinhlong1_1500.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh THVL" tvg-logo="https://mytv.com.vn/upload/channel/24.png" tvg-id="vinhlong1hd" ,THVL1 HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/vinhlong1_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source=" https://tshift.fptplay.net/dvr/vinhlong2_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh THVL" tvg-logo="https://mytv.com.vn/upload/channel/28.png" tvg-id="vinhlong2hd" ,THVL2 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda2/vinhlong2_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vinhlong3_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh THVL" tvg-logo="https://mytv.com.vn/upload/channel/29.png" tvg-id="vinhlong3hd" ,THVL3 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda2/vinhlong3_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/vinhlong4_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🏷️ | Kênh THVL" tvg-logo="https://mytv.com.vn/upload/channel/57.png" tvg-id="vinhlong4hd" ,THVL4 HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda3/vinhlong4hd_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🎙️ | Kênh MUSIC" tvg-logo="http://mtvwe.com/images/logo.png?r=12413" tvg-id="mtvhd" , MTV Việt Nam HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/mtv_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🎙️ | Kênh MUSIC" tvg-logo="https://chungmaster.github.io/logo/inthebox/musicbox.png" tvg-id="musicbox", Music Box
https://livecdn.fptplay.net/hda3/music_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🎙️ | Kênh MUSIC" tvg-logo="https://chungmaster.github.io/logo/kpopsexy.png" ,Sexy Kpop TV
https://srv1.zcast.com.br/kpoptv/kpoptv/playlist.m3u8
#EXTINF:-1 group-title="🎙️ | Kênh MUSIC" tvg-logo="https://logos-download.com/wp-content/uploads/2020/06/1HD_Music_Television_Logo.png" ,1HD Music
http://1hdru-hls-otcnet.cdnvideo.ru/onehdmusic/tracks-v1a1/index.m3u8
#EXTINF:-1 group-title="🎙️ | Kênh MUSIC" tvg-logo="https://static.wikia.nocookie.net/tvfan/images/5/57/1920px-VIVA_Logo_1993-1998.png" tvg-id="VIVARussia.ru" ,VIVA Russia
https://live.prd.dlive.tv/hls/live/viva-russia.m3u8
#EXTINF:-1 group-title="🎙️ | Kênh MUSIC" tvg-logo="https://30a.com/wp-content/themes/30atheme/images/logo.png" ,30A Music
http://30a-tv.com/music.m3u8
#EXTINF:-1 group-title="🎙️ | Kênh MUSIC" tvg-logo="https://cdn-eahpp.nitrocdn.com/RCzkBRaujYOPLqTQplPIsvEJsfblUOFF/assets/static/optimized/rev-8233f16/wp-content/uploads/2021/11/Vevo-Pop.png" ,Vevo Pop
https://dai2.xumo.com/amagi_hls_data_xumo1212A-redboxvevo/CDN/playlist.m3u8
#EXTINF:-1 group-title="🎙️ | Kênh MUSIC" tvg-logo="https://www.stingray.com/sites/www.stingray.com/files/entertainment_products/logos/stingray-karaoke-white-vertical.png" ,Stingray Karaoke HD 
https://stirr.ott-channels.stingray.com/karaoke/master.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/hbo_1500.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🎞 | Kênh MOVIES" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/6/67/HBO_New_Logo.png" tvg-id="hbohd" ,HBO HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/hbo_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/cinemax_1500.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🎞 | Kênh MOVIES" tvg-logo="https://qnet.com.vn/data/banners/rci1588038734.png" tvg-id="cinemaxhd" ,Cinemax HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/cinemax_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/axnhd_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🎞 | Kênh MOVIES" tvg-logo="https://mytv.com.vn/upload/channel/177.png" tvg-id="axnhd" ,AXN HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://livecdn.fptplay.net/hda3/axnhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/warnertv_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🎞 | Kênh MOVIES" tvg-logo="https://imgur.com/9qJI1Mg.png" tvg-id="warnertvhd" ,Warner Bros. TV HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda3/warnertv_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/kixhd_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🎞 | Kênh MOVIES" tvg-logo="http://console.celestialtiger.com/images/upload/693c8d81ab95b24b2549a1d9832efd42b6ff8e6c.png" tvg-id="kix" ,KIX HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda1/kixhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/cinemawork_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🎞 | Kênh MOVIES" tvg-logo="https://qnet.com.vn/data/banners/hxa1379060076.png" tvg-id="cinemaworldhd" ,CinemaWorld HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda2/cinemawork_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🎞 | Kênh MOVIES" tvg-logo="https://www.hitstv.com/img/hits-movies-logo.png" tvg-id="hits" ,HITS HD
http://gg.gg/hits_vthanh
#EXTINF:-1 group-title="🎞 | Kênh MOVIES" tvg-logo="https://image.xumo.com/v1/providers/provider/2186/300x300.png?type=color_onBlack" ,Hallmark Movies & More
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://dai2.xumo.com/amagi_hls_data_xumo1212A-rokuhallmark/CDN/playlist.m3u8
#EXTINF:-1 group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="https://chungmaster.github.io/logo/ant_thbp3.png" tvg-id="animaxhd" ,BPTV3 - ANT
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sda/ant_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/animaxport_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="https://chungmaster.github.io/logo/ott/animax.png" tvg-id="animaxhd" ,Animax HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda3/animaxport_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/boomerang_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/102.png" tvg-id="boomerang" ,Boomerang HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda3/boomerang_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/108.png?rand=246" tvg-id="cbeebies" ,BBC Cbeebies HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda3/cbeebies_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/cartoonnetworkhd_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="https://chungmaster.github.io/logo/cartoonnetwork.png" tvg-id="cartoonhd" ,Cartoon Network HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda3/cartoonnetworkhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="babytvhd" tvg-logo="https://www.babytv.com/app/uploads/2019/12/LogoBabyTV-2019.png" group-title="👼 | Kênh KIDS & CARTOON",BabyTV HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda3/babytvhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="babyfirst" tvg-logo="https://chungmaster.github.io/logo/babyfirsttv.png" group-title="👼 | Kênh KIDS & CARTOON",Baby First HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
http://livecdn.fptplay.net/hda1/babyfirst_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="dreamworks" tvg-logo="http://www.dreamworks-asia.com/images/dwalogo.png" group-title="👼 | Kênh KIDS & CARTOON",DreamWorks HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda3/dreamworks_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="https://chungmaster.github.io/logo/davincilogo.png" tvg-id="davinci" ,Da Vinci Kids Learning HD - FPT 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda2/davincihd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="davinci" tvg-logo="https://chungmaster.github.io/logo/davincilogo.png" group-title="👼 | Kênh KIDS & CARTOON" ,Da Vinci Kids Learning HD - HTVC
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
http://htv-drm-live-cdn.fptplay.net/CDN-FPT02/DAVINCY-HD-1080p/playlist.m3u8
#EXTINF:-1 group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="https://www.cocoro.tv/channels/co/channel-banner.png" ,Cocoro HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://4ea7abcc97144832b81dc50c6e8d6330.mediatailor.us-east-1.amazonaws.com/v1/master/44f73ba4d03e9607dcd9bebdcb8494d86964f1d8/Roku_Cocoro/playlist.m3u8
#EXTINF:-1 group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="https://www.ani-box.com/styles/sky-modern-a1/images/anibox-main-logo-518-140.png" ,ANI-BOX
https://56a6b9c3b5417.streamlock.net/livestream/smil:aniboxlive.smil/playlist.m3u8
#EXTINF:-1 group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="https://i.imgur.com/GETG2sS.png" ,CONtv Anime
https://dai2.xumo.com/amagi_hls_data_xumo-host-contvanime-junction/CDN/playlist.m3u8
#EXTINF:-1 group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="http://static.epg.best/sa/NickJr.sa.png" ,Nickelodeon Junior
http://gg.gg/NickelodeonJR
#EXTINF:-1 group-title="👼 | Kênh KIDS & CARTOON" tvg-logo="https://i0.wp.com/tokusatsunetwork.com/wp-content/uploads/2020/03/tsu-e1584362198575.png" ,TokuSHOUTsu
http://gg.gg/TokuSHOUTsu
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://chungmaster.github.io/logo/ott/rockextreme.png" tvg-id="blueantext" ,ROCK Extreme HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda1/blueantext_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://chungmaster.github.io/logo/ott/rockentertainment.png" tvg-id="blueantent" ,ROCK Entertainment HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda1/blueantent_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/276.png" tvg-id="afnhd" ,Asian Food Channel HD - FPT
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda1/afchd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/276.png" tvg-id="afnhd" ,Asian Food Channel HD - HTVC
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
http://htv-drm-live-cdn.fptplay.net/CDN-FPT02/AFC-HD-1080p/playlist.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/travelliving_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://www.tlc-tw.com/images/logo.png" tvg-id="tlchd" ,TLC HD - The Learning Channel
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda2/travelliving_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/animalplanet_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://qnet.com.vn/data/banners/rpw1548994974.png" tvg-id="animalhd" ,Animal Planet HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda2/animalplanet_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="outdoorfhd" tvg-logo="https://www.outdoorchannel.com/network/img/odc/logo.png" group-title="🗺️ | Kênh Quốc Tế" ,Outdoor Channel HD 
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda1/outdoorfhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="ngchd" tvg-logo="https://www.natgeotv.com/App_Resources2/Themes/2012/Images/Main/natgeo.png" group-title="🗺️ | Kênh Quốc Tế" ,National Geographic Channel HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda2/natgeohd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="ngwhd" tvg-logo="https://www.natgeotv.com/App_Resources2/Themes/2012/Images/Main/natgeowild.png" group-title="🗺️ | Kênh Quốc Tế" ,Nat Geo WILD HD - FPT
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda3/natgeowild_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="ngwhd" tvg-logo="https://www.natgeotv.com/App_Resources2/Themes/2012/Images/Main/natgeowild.png" group-title="🗺️ | Kênh Quốc Tế" ,Nat Geo WILD HD - HTVC
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
http://htv-drm-live-cdn.fptplay.net/CDN-FPT02/NATGEOWILD-HD-1080p/playlist.m3u8
#EXTINF:-1 tvg-id="discoveryhd" tvg-logo="https://qnet.com.vn/data/banners/pob1572421124.png" group-title="🗺️ | Kênh Quốc Tế" catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/discovrery_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" ,Discovery Channel HD - FPT
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda2/discovery_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 tvg-id="discoveryhd" tvg-logo="https://qnet.com.vn/data/banners/pob1572421124.png" group-title="🗺️ | Kênh Quốc Tế" ,Discovery Channel HD - HTVC
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
http://htv-drm-live-cdn.fptplay.net/CDN-FPT02/DISCOVERY-HD-1080p/playlist.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/discoveryasia_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🗺️ | Kênh Quốc Tế" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/253.png" tvg-id="discoveryasiahd" ,Discovery Asia HD
https://livecdn.fptplay.net/hda2/discoveryasia_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/bbcearth_1000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🗺️ | Kênh Quốc Tế" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/252.png" tvg-id="bbcearth" ,BBC Earth HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda2/bbcearth_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 catchup="append" catchup-days="3" catchup-source="https://tshift.fptplay.net/dvr/bbclifestyle_2000.stream/chunks_dvr_range-${start}-${offset}.m3u8" group-title="🗺️ | Kênh Quốc Tế" tvg-logo="http://mod.cht.com.tw/img/channel/channelpic/260.png" tvg-id="bbclifestyle" ,BBC Lifestyle HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/sdb/bbclifestyle_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="historyhd" tvg-logo="https://chungmaster.github.io/logo/history.png" group-title="🗺️ | Kênh Quốc Tế" ,History HD - HTVC
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36  
http://gg.gg/History1080p
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://chungmaster.github.io/logo/davincilogo.png" tvg-id="davincihd" ,Da Vinci Kids Learning HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda2/davincihd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://img.hplus.com.vn/355x200/poster/2021/09/30/322227-DMAX-NEW2.png" tvg-id="dmaxhd" ,DMAX
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
http://gg.gg/DMAX720p
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Fashion_TV_logo.svg/250px-Fashion_TV_logo.svg.png" tvg-id="fashionhd" ,Fashion TV HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda2/fashiontvhd_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/f/ff/BBC_News.svg/640px-BBC_News.svg.png" tvg-id="bbcworldnews" ,BBC World News HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36  
https://livecdn.fptplay.net/sdb/bbcnew_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/CNN.svg/200px-CNN.svg.png" tvg-id="cnn" ,CNN HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36  
https://livecdn.fptplay.net/sdb/cnn_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://mytv.com.vn/upload/channel/50.png" tvg-id="nhk_world" ,NHK World Japan HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36  
https://livecdn.fptplay.net/hda2/nhkworld_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="http://fboximages.fptplay.net.vn/Channel/iconChannel/abcaustralia_vdsl.png" tvg-id="abcaustralia" ,ABC Australia
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/sdb/australiaplus_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://imgstatic.vtvcab.vn/logos/DW_CHANNEL_M.png"  tvg-id="dw" ,DW News HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36 
https://livecdn.fptplay.net/hda2/dwenglish_vhls.smil/chunklist_b5000000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://chungmaster.github.io/logo/cnbc.png" ,CNBC
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36  
https://livecdn.fptplay.net/sdb/cnbc_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://www.arirang.com/images/index/arirang.png" tvg-id="arirang" ,Ariang KOREA  TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/arirang_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://imgstatic.vtvcab.vn/logos/KBS_WORLD_M.png" tvg-id="kbsworld" ,KBS World HD
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/hda3/kbs_4000.stream/chunklist.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://mytv.com.vn/upload/channel/184.png" tvg-id="bloomberg" ,Bloomberg TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/bloomberg_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://imgstatic.vtvcab.vn/logos/CNA_M.png" tvg-id="cna" ,Channel News Asia
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/newsasia_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://mytv.com.vn/upload/channel/137.png" tvg-id="france24eng" ,France 24 English
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/france24_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 group-title="🗺️ | Kênh Quốc Tế" tvg-logo="https://mytv.com.vn/upload/channel/65.png" tvg-id="tv5monde_asie" ,TV5 Monde Asie
#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
https://livecdn.fptplay.net/sdb/tv5_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="http://www.arirang.com/images/index/arirang.png" group-title="🌎 | Kênh Worldwide" ,Ariang KOREA 
https://amdlive-ch01-ctnd-com.akamaized.net/arirang_1ch/smil:arirang_1ch.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/50.png" group-title="🌎 | Kênh Worldwide" ,NHK World Japan HD
https://nhkworld.webcdn.stream.ne.jp/www11/nhkworld-tv/global/2003458/live.m3u8
#EXTINF:-1 tvg-logo="https://imgstatic.vtvcab.vn/logos/CNA_M.png" group-title="🌎 | Kênh Worldwide" ,Channel News Asia HD 
https://d2e1asnsl7br7b.cloudfront.net/7782e205e72f43aeb4a48ec97f66ebbe/index_5.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/184.png" group-title="🌎 | Kênh Worldwide" ,Bloomberg TV Asia HD 
https://www.bloomberg.com/media-manifest/streams/asia.m3u8
#EXTINF:-1 tvg-logo="https://static.france24.com/meta_og_twcards/jsonld_publisher.png" group-title="🌎 | Kênh Worldwide" ,France 24 HD
https://static.france24.com/live/F24_FR_HI_HLS/live_tv.m3u8
#EXTINF:-1 tvg-logo="https://www.smithsonianchannel.ca/wp-content/uploads/2018/10/smithsonian-logo-header.png" group-title="🌎 | Kênh Worldwide" ,Smithsonian Channel HD
https://smithsonianaus-samsungau.amagi.tv/playlist1080p.m3u8
#EXTINF:-1 tvg-logo="https://chungmaster.github.io/logo/food52.png" group-title="🌎 | Kênh Worldwide" ,Food52 TV HD 
https://dai2.xumo.com/amagi_hls_data_xumo1212A-food52/CDN/1280x720_5000000/index.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/1gqn4GQ.png" group-title="🌎 | Kênh Worldwide" ,The Design Network
https://dai2.xumo.com/amagi_hls_data_xumo1212A-redboxthedesignnetwork/CDN/playlist.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/574px-NASA_logo.svg.png" group-title="🌎 | Kênh Worldwide" ,NASA TV HD 
https://ntv1.akamaized.net/hls/live/2014075/NASA-NTV1-HLS/master.m3u8
#EXTINF:-1 tvg-logo="https://www.newsmaxtv.com/CMSScripts/NewsmaxTV/images/logos/Newsmax-TV-White.png" group-title="🌎 | Kênh Worldwide" ,Newsmax TV
https://nmxlive.akamaized.net/hls/live/529965/Live_1/index_720.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/CBS_News.svg/1200px-CBS_News.svg.png"  group-title="🌎 | Kênh Worldwide" ,CBS NEWS 
https://dai.google.com/linear/hls/event/Sid4xiTQTkCT1SLu6rjUSQ/master.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/TRT_World_logo.svg/640px-TRT_World_logo.svg.png" group-title="🌎 | Kênh Worldwide" , TRT World HD
https://tv-trtworld.live.trt.com.tr/master.m3u8
#EXTINF:-1 tvg-logo="https://chungmaster.github.io/logo/sbs_viceland.png" group-title="🌎 | Kênh Worldwide" ,SBS Viceland HD
https://sbs-live.akamaized.net/hls/live/2002828/channel2/open/master_1800K.m3u8
#EXTINF:-1 tvg-logo="https://cdn.one.accedo.tv/files/5e60392da0e845000ffa83eb?sessionKey=01FB9FENYXP3FKNJWMZ5Z9JWHA1178466205#asset" group-title="🌎 | Kênh Worldwide" ,Australia Channel HD
https://austchannel-live.akamaized.net/hls/live/2002729/austchannel-news/master.m3u8
#EXTINF:-1 tvg-logo="http://static.epg.best/au/ABCNews24.au.png" group-title="🌎 | Kênh Worldwide" ,ABC News 24
https://abc-iview-mediapackagestreams-2.akamaized.net/out/v1/6e1cc6d25ec0480ea099a5399d73bc4b/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Deutsche_Welle_Logo.svg/743px-Deutsche_Welle_Logo.svg.png"  group-title="🌎 | Kênh Worldwide" ,DW Deutsch+ 
https://dwamdstream105.akamaized.net/hls/live/2015531/dwstream105/index.m3u8
#EXTINF:-1 tvg-logo="https://ui.cgtn.com/static/ng/resource/images/header_icon/cgtn2020_logo.png" group-title="🌎 | Kênh Worldwide" ,CGTN English
https://live.cgtn.com/1000/prog_index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/d/d6/CGTN_Documentary_logo.png" group-title="🌎 | Kênh Worldwide" ,CGTN Documentary
https://livedoc.cgtn.com/1000d/prog_index.m3u8
#EXTINF:-1 tvg-logo="https://cdnen.rt.com/static/img/logo.png" group-title="🌎 | Kênh Worldwide" ,RT News HD
https://rt-glb.gcdn.co/live/rtnews/playlist_4500Kb.m3u8
#EXTINF:-1 tvg-logo="https://rtd.rt.com/s/redesign/pub/img/logo.png" group-title="🌎 | Kênh Worldwide" ,RT Documentary HD
https://rt-rtd.gcdn.co/live/rtdoc/playlist_4500Kb.m3u8
#EXTINF:-1 tvg-logo="https://www.skynews.com.au/wp-content/themes/newscorpau-news-dna/dist/images/logos/skynews.svg" group-title="🌎 | Kênh Worldwide",Sky News Australia HD 
https://skynewsau-live.akamaized.net/hls/live/2002691/skynewsau-extra3/master.m3u8
#EXTINF:-1 tvg-logo="http://i.imgur.com/wzBD6fy.png"  group-title="🌎 | Kênh Worldwide" ,TMZ News
https://dai2.xumo.com/xumocdn/p=roku/amagi_hls_data_xumo1234A-tmz/CDN/1280x720_5000000/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Global_News.svg/1200px-Global_News.svg.png" group-title="🌎 | Kênh Worldwide" ,Global News
https://live.corusdigitaldev.com/groupd/live/49a91e7f-1023-430f-8d66-561055f3d0f7/live.isml/live-audio_1=96000-video=2499968.m3u8
#EXTINF:-1 tvg-logo="https://img.nbc.com/sites/nbcunbc/files/images/2020/9/14/NBCNewsNow-Logo-White-344x300.png" group-title="🌎 | Kênh Worldwide" ,NBC News Now 
https://dai2.xumo.com/amagi_hls_data_xumo1212A-xumo-nbcnewsnow/CDN/master.m3u8
#EXTINF:-1 tvg-logo="https://lovenature.com/wp-content/uploads/2020/08/love-nature-logo_peacock.png" group-title="🌎 | Kênh Worldwide" ,LoveNature HD
http://bamus-eng-roku.amagi.tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://chungmaster.github.io/logo/jasmintv.png" group-title="🌎 | Kênh Worldwide" ,Jasmin TV HD
http://109.71.162.112:1935/live/hd.jasminchannel.stream/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh UHD 4K" tvg-logo="https://chungmaster.github.io/logo/LoveNature4K.png",Love Nature 4K
https://d18dyiwu97wm6q.cloudfront.net/playlist2160p.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh UHD 4K" tvg-logo="https://play-lh.googleusercontent.com/MDqkIoSsj4bFmxTa8082V7c6ed9akFZwdPk0gLxDFYK4XoRaOSmkuTC67qSrdMAO3Wk",Bloomberg+ Business 4K
https://bloomberg-bloombergtv-1-gb.samsung.wurl.com/manifest/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh UHD 4K" tvg-logo="https://mytv.com.vn/upload/channel/162.png",FashionTV UHD
https://fash2043.cloudycdn.services/slive/ftv_ftv_4k_hevc_73d_42080_default_466_hls.smil/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh UHD 4K" tvg-logo="https://images.squarespace-cdn.com/content/55f79bede4b0917adab94052/1611005142885-LJJTKDYMQJ7S6SQ8L182/Program-Guide-Channel-Logo_Loupe.png",LOUPE 4K
http://d2dw21aq0j0l5c.cloudfront.net/playlist_3840x2160.m3u8
#EXTINF:-1 tvg-id="hanoi1" tvg-logo="https://mytv.com.vn/upload/channel/190.png" group-title="🗼 | Kênh Địa Phương VN",HN1 HD - Truyền hình Hà Nội
http://cdn.hntv.mediatech.vn/hntvlive/tv1live480.m3u8
#https://live.hanoitv.vn/hntvlive/tv1live.m3u8
#EXTINF:-1 tvg-id="hanoi2"  tvg-logo="https://mytv.com.vn/upload/channel/193.png" group-title="🗼 | Kênh Địa Phương VN",HN2 HD - Truyền hình Hà Nội
https://live.hanoitv.vn/hntvlive/tv2live.m3u8
#EXTINF:-1 tvg-id="quangninh1"  tvg-logo="https://media.baoquangninh.com.vn/upload/files/logo/logotrangchu1.png" group-title="🗼 | Kênh Địa Phương VN",QTV1 - Truyền hình Quảng Ninh
https://qtv.vncdn.vn/qtvlive/tv1live.m3u8
#EXTINF:-1 tvg-id="quangninh3"  tvg-logo="https://media.baoquangninh.com.vn/upload/files/logo/logotrangchu2.png" group-title="🗼 | Kênh Địa Phương VN",QTV3 - Truyền hình Quảng Ninh
https://qtv.vncdn.vn/qtvlive/tv3live.m3u8
#EXTINF:-1 tvg-id="bacgiang"  tvg-logo="https://mytv.com.vn/upload/channel/981.png" group-title="🗼 | Kênh Địa Phương VN",BGTV HD - Truyền hình Bắc Giang
https://live.bacgiangtv.vn/bgtvlive/tv1live.m3u8
#EXTINF:-1 tvg-id="hungyen"  tvg-logo="https://mytv.com.vn/upload/channel/892.png" group-title="🗼 | Kênh Địa Phương VN",HYTV  HD - Truyền hình Hưng Yên
https://live.hungyentv.vn/hytvlive/tv1live.m3u8
#EXTINF:-1 tvg-id="laocai"  tvg-logo="http://laocaitv.vn/lib/images/footer-logo.png" group-title="🗼 | Kênh Địa Phương VN",Truyền hình Lào Cai
http://cdn.3ssoft.vn/livetv/laocaitv/laocaitv/index.m3u8
#EXTINF:-1 tvg-id="yenbai"  tvg-logo="http://yenbaitv.org.vn/modules/frontend/themes/ptthyb/images/logo.png" group-title="🗼 | Kênh Địa Phương VN",Truyền hình Yên Bái
https://yenbaitv.org.vn/hls/livestream.m3u8
#EXTINF:-1 tvg-id="sonla"  tvg-logo="https://mytv.com.vn/upload/channel/261.png" group-title="🗼 | Kênh Địa Phương VN",STV HD  - Truyền hình Sơn La
http://118.107.85.5:1935/live/smil:STV.smil/playlist.m3u8
#EXTINF:-1 tvg-id="langson"  tvg-logo="http://www.langsontv.vn/templates/frontend/lstv/Assets/img/logo_lstv.png" group-title="🗼 | Kênh Địa Phương VN",LSTV HD - Truyền hình Lạng Sơn
http://live.langsontv.vn/lstvlive/tv1live.m3u8
#EXTINF:-1 tvg-id="tuyenquang"  tvg-logo="https://mytv.com.vn/upload/channel/221.png" group-title="🗼 | Kênh Địa Phương VN",TTV - Truyền hình Tuyên Quang
https://live.tuyenquangtv.vn/hls/ttv.m3u8
#EXTINF:-1 tvg-id="phutho"  tvg-logo="https://mytv.com.vn/upload/channel/192.png" group-title="🗼 | Kênh Địa Phương VN",PTV - Truyền hình Phú Thọ
https://livecdn.fptplay.net/sda/phutho_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="hoabinh"  tvg-logo="https://mytv.com.vn/upload/channel/281.png" group-title="🗼 | Kênh Địa Phương VN",HBTV - Truyền hình Hòa Bình
http://hoabinhtvlive.746b3ddb.cdnviet.com/hoabinhtv/playlist.m3u8
#EXTINF:-1 tvg-id="ninhbinh"  tvg-logo="https://nbtv.vn/templates/frontend/nbtv/Assets/img/logo.png" group-title="🗼 | Kênh Địa Phương VN",Truyền hình Ninh Bình
https://nbtv.vncdn.vn/nbtvlive/tv1live.m3u8
#EXTINF:-1 tvg-id="haiphong"  tvg-logo="https://mytv.com.vn/upload/channel/161.png" group-title="🗼 | Kênh Địa Phương VN",THP HD  - Truyền hình Hải Phòng
https://live.thhp.vn/thp/index.m3u8
#EXTINF:-1 tvg-id=""  tvg-logo="https://chungmaster.github.io/logo/THP+.png" group-title="🗼 | Kênh Địa Phương VN",THP+ HD - Truyền hình Hải Phòng +
https://live.thhp.vn/hls/thpplus/index.m3u8
#EXTINF:-1 tvg-id="bacninh"  tvg-logo="https://mytv.com.vn/upload/channel/992.png" group-title="🗼 | Kênh Địa Phương VN",BTV HD - Truyền hình Bắc Ninh
http://118.107.85.4:1935/live/smil:BTV.smil/playlist.m3u8
#EXTINF:-1 tvg-id="namdinh"  tvg-logo="https://mytv.com.vn/upload/channel/181.png" group-title="🗼 | Kênh Địa Phương VN",NTV - Truyền hình Nam Định
https://livecdn.fptplay.net/sdc/namdinh_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="hanam"  tvg-logo="http://hanamtv.vn/template/default/images/logo.png" group-title="🗼 | Kênh Địa Phương VN",THHN - Truyền hình Hà Nam
https://mediatech.vncdn.vn/thhnlive/tv1live.m3u8
#EXTINF:-1 tvg-id="vinhphuc"  tvg-logo="http://vinhphuctv.vn/Portals/4/images/logo-vp.png" group-title="🗼 | Kênh Địa Phương VN",VP HD  - Truyền hình Vĩnh Phúc
http://vinhphuctv.vn:8090/vinhphuclive/web.stream_720p/playlist.m3u8
#EXTINF:-1 tvg-id="laichau"  tvg-logo="https://mytv.com.vn/upload/channel/251.png" group-title="🗼 | Kênh Địa Phương VN",LTV HD  - Truyền hình Lai Châu 
http://123.31.36.68/live.m3u8?c=vstv361&q=high&type=tv&gcId=1532&userId=&deviceId=&deviceType=&location=NA&requestTime=1586309420781&pkg=pkg11
#EXTINF:-1 tvg-id="dienbien"  tvg-logo="https://mytv.com.vn/upload/channel/271.png" group-title="🗼 | Kênh Địa Phương VN",ĐTV - Truyền hình Điện Biên
https://truyenhinh.vnptvas.vn/live.m3u8?c=vstv362&q=high&type=tv&gcId=1532&userId=&deviceId=&deviceType=&location=NA&requestTime=1586309420781&pkg=pkg11
#EXTINF:-1 tvg-id="caobang"  tvg-logo="https://mytv.com.vn/upload/channel/111.png" group-title="🗼 | Kênh Địa Phương VN",CRTV - Truyền hình Cao Bằng
http://118.107.85.4:1935/live/smil:CRTV.smil/playlist.m3u8
#EXTINF:-1 tvg-id="backan"  tvg-logo="https://mytv.com.vn/upload/channel/971.png" group-title="🗼 | Kênh Địa Phương VN",TBK - Truyền hình Bắc Kạn HD
https://livecdn.fptplay.net/sdb/backan_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="thainguyen"  tvg-logo="https://mytv.com.vn/upload/channel/203.png" group-title="🗼 | Kênh Địa Phương VN",TN1 HD - Truyền hình Thái Nguyên
https://streaming.thainguyentv.vn/hls/livestream.m3u8
#EXTINF:-1 tvg-id="thainguyen2"  tvg-logo="https://8387a88d1b.vws.vegacdn.vn/Media/files/channels/poster_1622021426channel2_TN%202.png" group-title="🗼 | Kênh Địa Phương VN",TN2 HD - Truyền hình Thái Nguyên
https://8387e1fb5a.vws.vegacdn.vn/live/thainguyen2/playlist.m3u8
#EXTINF:-1 tvg-id="thaibinh"  tvg-logo="http://thaibinhtv.vn/templates/frontend/tbtv/Assets/img/logo.png" group-title="🗼 | Kênh Địa Phương VN",TBTV HD - Truyền hình Thái Bình
http://cdn.tbtv.mediatech.vn/tbtvlive/tv1live.m3u8
#EXTINF:-1 tvg-id="haiduong"  tvg-logo="https://rsstv.gviet.vn/sctv/157/595/1565944958841.png" group-title="🗼 | Kênh Địa Phương VN",THD SD - Truyền hình Hải Dương
https://livecdn.fptplay.net/sdc/haiduong_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="hagiang"  tvg-logo="https://mytv.com.vn/upload/channel/231.png" group-title="🗼 | Kênh Địa Phương VN",HGTV - Truyền hình Hà Giang
https://truyenhinh.vnptvas.vn/live.m3u8?c=vstv365&q=high&type=tv&token=LX-ibJYRUq9pflRtYAxfYQ&time=1586395820&gcId=1532&userId=&deviceId=&deviceType=&location=NA&requestTime=1586309420781&pkg=pkg11
#EXTINF:-1 tvg-id="thanhhoa"  tvg-logo="https://mytv.com.vn/upload/channel/361.png" group-title="🗼 | Kênh Địa Phương VN",TTV - Truyền hình Thanh Hóa
http://123.31.36.68/live.m3u8?c=vstv208&q=high&type=tv&token=1111&time=1586395820&gcId=1532&userId=&deviceId=&deviceType=&location=NA&requestTime=1586309420781&pkg=pkg11
#EXTINF:-1 tvg-id="hatinh"  tvg-logo="https://hatinhtv.vn/img/logo-footer.png" group-title="🗼 | Kênh Địa Phương VN",HTTV - Truyền hình Hà Tĩnh
https://hatinhtv.vn/hls/httv.m3u8
#EXTINF:-1 tvg-id="nghean"  tvg-logo="https://mytv.com.vn/upload/channel/phpKczJ13_5d75cc55e9d4a.png" group-title="🗼 | Kênh Địa Phương VN",Truyền hình Nghệ An
https://live.truyenhinhnghean.vn/hls/na1/index.m3u8
#EXTINF:-1 tvg-id="danang1"  tvg-logo="http://www.drt.danang.vn/images/drt1.png" group-title="🗼 | Kênh Địa Phương VN",DaNangTV1 - Truyền hình Đà Nẵng
https://livecdn.fptplay.net/sdc/danang1_2000.stream/chunklist_b2500000.m3u8
#http://drtdnglive.e49a7c38.cdnviet.com/livedrt1/playlist.m3u8
#EXTINF:-1  tvg-id="danang2" tvg-logo="http://www.drt.danang.vn/images/drt2.png" group-title="🗼 | Kênh Địa Phương VN",DaNangTV2 - Truyền hình Đà Nẵng
https://livecdn.fptplay.net/sdc/danang2_hls.smil/chunklist_b2800000.m3u8
#http://drtdnglive.e49a7c38.cdnviet.com/livestream/playlist.m3u8
#EXTINF:-1 tvg-id="hue"  tvg-logo="https://chungmaster.github.io/logo/trthue.png" group-title="🗼 | Kênh Địa Phương VN",TRT - Truyền hình Thừa Thiên Huế
https://live.trt.com.vn/TRT-Online/playlist.m3u8
#EXTINF:-1 tvg-id="binhthuan" tvg-logo="https://img.hplus.com.vn/728x409/banner/2018/06/06/386181-Binh-Thuan.png" group-title="🗼 | Kênh Địa Phương VN",BTV HD - Truyền hình Bình Thuận
http://202.43.109.144:1935/thbttv/bttv/chunklist_w1111614173.m3u8
#EXTINF:-1 tvg-logo="https://chungmaster.github.io/logo/BTV6_QHSP.png" group-title="🗼 | Kênh Địa Phương VN",BTV6 - Truyền hình Bình Thuận
https://livecdn.fptplay.net/sdb/quehuongshop_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="ninhthuan"  tvg-logo="https://mytv.com.vn/upload/channel/851.png" group-title="🗼 | Kênh Địa Phương VN",NTV - Truyền hình Ninh Thuận
https://livecdn.fptplay.net/sda/ninhthuan_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="phuyen" tvg-logo="https://mytv.com.vn/upload/channel/781.png" group-title="🗼 | Kênh Địa Phương VN",PTP - Truyền hình Phú Yên 
https://livecdn.fptplay.net/sda/phuyen_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="khanhhoa" tvg-logo="http://ktv.org.vn/wp-content/themes/ktv/assets/img/logo.png" group-title="🗼 | Kênh Địa Phương VN",KTV - Truyền hình Khánh Hòa
http://210.245.20.94/ktv.m3u8
#EXTINF:-1 tvg-id="quangbinh" tvg-logo="https://mytv.com.vn/upload/channel/731.png" group-title="🗼 | Kênh Địa Phương VN",QBTV - Truyền hình Quảng Bình
https://livecdn.fptplay.net/sda/quangbinh_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="quangngai" tvg-logo="https://mytv.com.vn/upload/channel/761.png" group-title="🗼 | Kênh Địa Phương VN",PTQ - Truyền hình Quảng Ngãi
http://118.107.85.5:1935/live/smil:PTQ.smil/playlist.m3u8
#EXTINF:-1 tvg-id="hue"   tvg-logo="https://img.hplus.com.vn/728x409/banner/2018/06/05/443495-QRT.png" group-title="🗼 | Kênh Địa Phương VN",QRT - Truyền hình Quảng Nam
http://113.161.6.157:8081/hls-live/livepkgr/_definst_/liveevent/livestream.m3u8
#EXTINF:-1 tvg-id="vungtau" tvg-logo="http://brt.vn/common/v1/images/logo-footer.png" group-title="🗼 | Kênh Địa Phương VN",BRT - Truyền hình Bà Rịa Vũng Tàu
https://livecdn.fptplay.net/sdc/bariavungtau_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/741.png" group-title="🗼 | Kênh Địa Phương VN",QRTV - Truyền hình Quảng Trị
https://livecdn.fptplay.net/sdc/quangtri_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="angiang" tvg-logo="http://atv.org.vn/lib/images/logo.png" group-title="🗼 | Kênh Địa Phương VN",ATV - Truyền hình An Giang
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/ANGIANG-SD-ABR/HTV-ABR/ANGIANG-SD-720p/playlist.m3u8
#EXTINF:-1 tvg-id="tiengiang" tvg-logo="http://www.thtg.vn/wp-content/themes/thtg/images/logo.png" group-title="🗼 | Kênh Địa Phương VN",THTG - Truyền hình Tiền Giang
http://123.25.238.45:1935/live/thtg/playlist.m3u8
#EXTINF:-1 tvg-id="haugiang"  tvg-logo="https://mytv.com.vn/upload/channel/951.png" group-title="🗼 | Kênh Địa Phương VN",HGV - Truyền hình Hậu Giang
https://livecdn.fptplay.net/sda/haugiang_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="http://tayninhtv.vn/public/Home/images/logo_ttv11.png" group-title="🗼 | Kênh Địa Phương VN",TTV11 HD - Truyền hình Tây Ninh
http://202.43.109.142:1935/ttv11/tntv/chunklist_w1452030890.m3u8
#EXTINF:-1 tvg-id="travinh" tvg-logo="https://mytv.com.vn/upload/channel/841.png" group-title="🗼 | Kênh Địa Phương VN",THTV - Truyền hình Trà Vinh
https://livecdn.fptplay.net/sdc/travinh_1000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/601.png" group-title="🗼 | Kênh Địa Phương VN", ĐNRTV1 - Truyền hình Đồng Nai
https://livecdn.fptplay.net/sda/dongnai1_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/602.png" group-title="🗼 | Kênh Địa Phương VN", ĐNRTV2 - Truyền hình Đồng Nai
https://livecdn.fptplay.net/hda4/dongnai2_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://chungmaster.github.io/logo/dnrtv3.png" group-title="🗼 | Kênh Địa Phương VN", ĐNRTV3 - Truyền hình Đồng Nai
http://gg.gg/dnrtv3_vieon
#EXTINF:-1 tvg-logo="https://static.skyshoptv.vn/catalog/logo.png" group-title="🗼 | Kênh Địa Phương VN", ĐNRTV9 (SKYshop TV) - Truyền hình Đồng Nai
https://livecdn.fptplay.net/sda/skymart_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="gialai"  tvg-logo="https://mytv.com.vn/upload/channel/811.png" group-title="🗼 | Kênh Địa Phương VN",THGL HD - Truyền hình Gia Lai
http://113.161.25.3:8134/hls/gialaitv/gialaitv.m3u8
#EXTINF:-1 tvg-id="kontum" tvg-logo="https://mytv.com.vn/upload/channel/821.png" group-title="🗼 | Kênh Địa Phương VN",KRT HD - Truyền hình Kon Tum
https://tv.kontumtv.vn/live/kontumtv/kontumtv.m3u8|Referer=https://kontumtv.vn/
#EXTINF:-1 tvg-id="daknong"  tvg-logo="https://mytv.com.vn/upload/channel/481.png" group-title="🗼 | Kênh Địa Phương VN",PTD - Truyền hình DakNong 
http://gg.gg/daknong
#EXTINF:-1 tvg-id="daklak"  tvg-logo="https://mytv.com.vn/upload/channel/471.png" group-title="🗼 | Kênh Địa Phương VN",PTD - Truyền hình DakLak 
https://livecdn.fptplay.net/sdc/daklak_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="lamdong"  tvg-logo="https://mytv.com.vn/upload/channel/491.png" group-title="🗼 | Kênh Địa Phương VN",LTV - Truyền hình Lâm Đồng
https://livecdn.fptplay.net/sdc/lamdong_2000.stream/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="bentre" tvg-logo="https://mytv.com.vn/upload/channel/711.png" group-title="🗼 | Kênh Địa Phương VN",THBT - Truyền hình Bến Tre
https://htv-drm-live-cdn.fptplay.net/CDN-FPT02/BENTRE-SD-ABR/HTV-ABR/BENTRE-SD-720p/playlist.m3u8
#EXTINF:-1 tvg-logo="https://thbl.vn/wp-content/themes/daith2019/assets/img/logo.png" group-title="🗼 | Kênh Địa Phương VN",BLTV - Truyền hình Bạc Liêu
https://livecdn.fptplay.net/sdc/baclieu_2000.stream/chunklist.m3u8
#EXTINF:-1 tvg-id="binhduong1" tvg-logo="https://img.hplus.com.vn/460x260/poster/2018/06/18/522019-BTV1.png" group-title="🗼 | Kênh Địa Phương VN",BTV1 HD - Truyền hình Bình Dương
https://livecdn.fptplay.net/hda3/btv1_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="binhduong2" tvg-logo="http://img.hplus.com.vn/460x260/poster/2018/06/18/245539-444791-BTV2.png" group-title="🗼 | Kênh Địa Phương VN",BTV2 HD - Truyền hình Bình Dương
https://livecdn.fptplay.net/hda3/btv2_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://static.wikia.nocookie.net/logos/images/1/1b/BTV3_HD_logo_2018-2019.png/revision/latest/scale-to-width-down/200?cb=20210124140333&path-prefix=vi" group-title="🗼 | Kênh Địa Phương VN",BTV3 HD - Truyền hình Bình Dương
https://livecdn.fptplay.net/sdb/binhduong3_hls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-id="binhduong4" tvg-logo="https://static.wikia.nocookie.net/logos/images/e/e9/BTV4_HD_logo.png/revision/latest/scale-to-width-down/1000?cb=20210122205643&path-prefix=vi" group-title="🗼 | Kênh Địa Phương VN",BTV4 HD - Truyền hình Bình Dương
https://livecdn.fptplay.net/hda2/btv4hd_vhls.smil/chunklist_b2500000.m3u8
#EXTINF:-1 tvg-logo="https://rsstv.gviet.vn/sctv/159/130/1581298778597.png" group-title="🗼 | Kênh Địa Phương VN",An Viên TV(BTV9 HD) - Truyền hình Bình Dương
http://gg.gg/AnVienTV
#EXTINF:-1 tvg-logo="http://img.btv.org.vn:81/upload/vod/25032020/1585128658_btv11.png" group-title="🗼 | Kênh Địa Phương VN",BTV11 (Top Home Shopping) - Truyền hình Bình Dương
https://livecdn.fptplay.net/sda/btv11_2000.stream/chunklist.m3u8
#EXTINF:-1 tvg-id="binhdinh" tvg-logo="https://mytv.com.vn/upload/channel/771.png" group-title="🗼 | Kênh Địa Phương VN",BTV - Truyền hình Bình Định
http://truyenhinhbinhdinhonline.dynns.com:8086/live.m3u8
#EXTINF:-1 tvg-id="binhphuoc1"  tvg-logo="https://media.baobinhphuoc.com.vn/upload/files/logo/bptv1.png" group-title="🗼 | Kênh Địa Phương VN",BPTV1 HD - Truyền hình Bình Phước
https://live.baobinhphuoc.com.vn/bptvlive/tv1live.m3u8
#EXTINF:-1 tvg-id="binhphuoc2"  tvg-logo="https://media.baobinhphuoc.com.vn/upload/files/logo/bptv2.png" group-title="🗼 | Kênh Địa Phương VN",BPTV2 HD - Truyền hình Bình Phước
https://live.baobinhphuoc.com.vn/bptvlive/tv2live.m3u8
#EXTINF:-1 tvg-logo="https://chungmaster.github.io/logo/ant_thbp3.png" group-title="🗼 | Kênh Địa Phương VN",BPTV3 (ANT)- Truyền hình Bình Phước
https://8387e1fb5a.vws.vegacdn.vn/live/binhphuoc3/playlist.m3u8
#EXTINF:-1 tvg-logo="http://thst.vn/Content/images/stv1.png" group-title="🗼 | Kênh Địa Phương VN",STV1 HD - Truyền hình Sóc Trăng
http://113.163.189.104:8135/hls-live/livepkgr/_definst_/liveevent/livestream.m3u8
#EXTINF:-1 tvg-logo="http://thst.vn/Content/images/stv2.png" group-title="🗼 | Kênh Địa Phương VN",STV2 HD - Truyền hình Sóc Trăng
http://113.163.189.104:8135/hls-live/livepkgr/_definst_/liveevent/livestreamstv2.m3u8
#EXTINF:-1 tvg-id="longan"  tvg-logo="http://la34.com.vn/wp-content/themes/la34/assets/img/logo.png" group-title="🗼 | Kênh Địa Phương VN",LA34 - Truyền hình Long An
http://113.161.229.13/hls-live/livepkgr/_definst_/liveevent/tv.m3u8
#EXTINF:-1 tvg-logo="https://chungmaster.github.io/logo/thdt1.png" group-title="🗼 | Kênh Địa Phương VN",THĐT1 HD - Truyền hình Đồng Tháp
http://118.69.169.41:1935/THDT/thdttv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://chungmaster.github.io/logo/thdt2.png" group-title="🗼 | Kênh Địa Phương VN",THDT2 - Truyền hình Đồng Tháp
http://202.43.109.145:1935/thdt2/thdt2/playlist.m3u8
#EXTINF:-1 tvg-id="camau" tvg-logo="https://mytv.com.vn/upload/channel/691.png" group-title="🗼 | Kênh Địa Phương VN",CTV - Truyền hình Cà Mau
http://tv.ctvcamau.vn/live/tv/tv.m3u8
#EXTINF:-1 tvg-id="cantho" tvg-logo="https://mytv.com.vn/upload/channel/651.png" group-title="🗼 | Kênh Địa Phương VN",THTPCT - Truyền hình Cần Thơ
https://mekongpassion.com/live/tv_web/playlist.m3u8
#EXTINF:-1 tvg-logo="https://img.hplus.com.vn/728x409/banner/2018/06/04/894592-KienGiang.png" group-title="🗼 | Kênh Địa Phương VN",KGTV - Truyền hình Kiên Giang 
https://tv.kgtv.vn/live/kgtv/kgtv.m3u8
#EXTINF:-1 tvg-logo="https://mytv.com.vn/upload/channel/683.png" group-title="🗼 | Kênh Địa Phương VN",KGTV1 - Truyền hình Kiên Giang
https://tv.kgtv.vn/live/kgtv1/kgtv1.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/RTHK_TV_31.svg/1200px-RTHK_TV_31.svg.png" group-title="🏷️ | Kênh HONGKONG",RTHK TV 31 (港台電視31)
https://cdn.hkdtmb.com/hls/31/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/RTHK_TV_32.svg/1024px-RTHK_TV_32.svg.png" group-title="🏷️ | Kênh HONGKONG",RTHK TV 32 (港台電視32)
https://cdn.hkdtmb.com/hls/32/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/RTHK_TV_33.svg/1024px-RTHK_TV_33.svg.png" group-title="🏷️ | Kênh HONGKONG",RTHK TV 33 (港台電視33)
https://cdn.hkdtmb.com/hls/33/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/zh/3/3a/HKIBC_logo.png" group-title="🏷️ | Kênh HONGKONG",Hong Kong International Business Channel (香港國際財經台)
https://cdn.hkdtmb.com/hls/76/index.m3u8
#EXTINF:-1 tvg-logo="http://www.hkopentv.com/assets/images/opentv_logo.png" group-title="🏷️ | Kênh HONGKONG",Hong Kong Open TV (香港開電視)
https://cdn.hkdtmb.com/hls/77/index.m3u8
#EXTINF:-1 tvg-logo="https://vignette.wikia.nocookie.net/evchk/images/8/88/Tvb_Jade_cap.png" group-title="🏷️ | Kênh HONGKONG",TVB Jade (翡翠台)
https://cdn.hkdtmb.com/hls/81/index.m3u8
#EXTINF:-1 tvg-logo="https://static.epg.best/hk/TVBJ2.hk.png" group-title="🏷️ | Kênh HONGKONG",TVB J2
https://cdn.hkdtmb.com/hls/82/index.m3u8
#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/hououinkami/AppleTV/master/ChannelLogo/Hongkong/TVB_News.png" group-title="🏷️ | Kênh HONGKONG",TVB News Channel (無綫新聞台)
https://cdn.hkdtmb.com/hls/83/index.m3u8
#EXTINF:-1 tvg-logo="https://vignette.wikia.nocookie.net/evchk/images/d/d2/TVB_Pearl.png" group-title="🏷️ | Kênh HONGKONG",TVB Pearl (明珠台)
https://cdn.hkdtmb.com/hls/84/index.m3u8
#EXTINF:-1 tvg-logo="https://raw.githubusercontent.com/hououinkami/AppleTV/master/ChannelLogo/Hongkong/TVB_Finance.png" group-title="🏷️ | Kênh HONGKONG",TVB Finance & Information Channel (無綫財經 · 資訊台)
https://cdn.hkdtmb.com/hls/85/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/ViuTVsix-logo.svg/1280px-ViuTVsix-logo.svg.png" group-title="🏷️ | Kênh HONGKONG",ViuTVsix
https://cdn.hkdtmb.com/hls/96/index.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/ViuTV_logo.svg/1280px-ViuTV_logo.svg.png" group-title="🏷️ | Kênh HONGKONG",ViuTV
https://cdn.hkdtmb.com/hls/99/index.m3u8
#EXTINF:-1  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/NHK_General_TV_logo.svg/1920px-NHK_General_TV_logo.svg.png" group-title="🏷️ | Kênh JAPAN",NHK総合
http://203.162.235.41:16903
#EXTINF:-1  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/NHK_Educational_TV_logo.svg/1200px-NHK_Educational_TV_logo.svg.png" group-title="🏷️ | Kênh JAPAN",NHK教育
http://203.162.235.41:16901
#EXTINF:-1  tvg-logo="https://www.nct9.co.jp/wordpress/wp-content/themes/nct/img/service/tv/ch/img_ch_nhkbs1.jpg" group-title="🏷️ | Kênh JAPAN",NHK BS1
http://220.158.149.28:8180/live/TV00000000000000000075@HHZT
#EXTINF:-1  tvg-logo="https://vignette.wikia.nocookie.net/logopedia/images/8/87/Q1_%281%29.jpg" group-title="🏷️ | Kênh JAPAN",NHK BSプレミアム
http://203.162.235.41:16910
#EXTINF:-1  tvg-logo="https://static.epg.best/jp/Asahi1.jp.png" group-title="🏷️ | Kênh JAPAN",テレビ朝日
http://203.162.235.41:16906
#EXTINF:-1  tvg-logo="https://static.epg.best/jp/TVTokyo.jp.png" group-title="🏷️ | Kênh JAPAN",テレビ東京
http://203.162.235.41:16908
#EXTINF:-1  tvg-logo="https://www.abu.org.my/images/articles/news/tbs_logo.jpg" group-title="🏷️ | Kênh JAPAN",TBSテレビ
http://203.162.235.41:16907
#EXTINF:-1  tvg-logo="https://upload.wikimedia.org/wikipedia/en/thumb/e/e9/Fuji_TV_logo.svg/150px-Fuji_TV_logo.svg.png" group-title="🏷️ | Kênh JAPAN",フジテレビ
http://203.162.235.41:16904
#EXTINF:-1  tvg-logo="https://static.epg.best/jp/NipponTV.jp.png" group-title="🏷️ | Kênh JAPAN",日テレ
http://203.162.235.41:16905
#EXTINF:-1  tvg-logo="https://startpoint.jp/wp-content/uploads/fb.jpg" group-title="🏷️ | Kênh JAPAN",日テレNEWS24
https://n24-cdn-live-b.ntv.co.jp/ch01/High.m3u8
#EXTINF:-1  tvg-logo="https://static.epg.best/jp/BSTBS.jp.png" group-title="🏷️ | Kênh JAPAN",BS TBS
http://203.162.235.41:16913
#EXTINF:-1  tvg-logo="https://www.bs-asahi.co.jp/wordpress/wp-content/themes/bs-master/img/no_image.png" group-title="🏷️ | Kênh JAPAN",BS 朝日
http://203.162.235.41:16914
#EXTINF:-1  tvg-logo="https://www.bsfuji.tv/top/common/img/head_logo.png" group-title="🏷️ | Kênh JAPAN",BSフジ
http://203.162.235.41:16911
#EXTINF:-1  tvg-logo="https://www.tv-tokyo.co.jp/information/blog/images/24606404907f11e880a6cbdce0444b13.jpg" group-title="🏷️ | Kênh JAPAN",BS 東京
http://203.162.235.41:16915
#EXTINF:-1  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/BS4_logo.svg/400px-BS4_logo.svg.png" group-title="🏷️ | Kênh JAPAN",BS 日テレ
http://203.162.235.41:16912
#EXTINF:-1  tvg-logo="https://www.abu.org.my/images/articles/news/tbs_logo.jpg" group-title="🏷️ | Kênh JAPAN",シネフィルWOWOW
http://203.162.235.41:16916
#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzO63HQCTp3Oj7ImD2GCoftjrujMZOZu5Ytw&usqp=CAU" group-title="🏷️ | Kênh JAPAN",Golf Network
http://203.162.235.41:16924
#EXTINF:-1  tvg-logo="https://www.gemtvasia.com/sites/gemtvasia.com/files/logos/logo-small.png" group-title="🏷️ | Kênh JAPAN",GEM TV
http://103.47.132.164/PLTV/88888888/224/3221227187/index.m3u8
#EXTINF:-1 tvg-id="FUJ.JP" tvg-logo="https://tvguide.myjcom.jp/monomedia/ch_logo/otd/logo-7FE4-081-400x400.png" group-title="🏷️ | Kênh JAPAN",Fuji TV (JOCX-DTV)
http://redlabmcdn.s.llnwi.net/jp04/ryowa7hd/playlist.m3u8
#EXTINF:-1 tvg-logo="https://tvguide.myjcom.jp/monomedia/ch_logo/otd/logo-7E87-091-400x400.png" group-title="🏷️ | Kênh JAPAN",Tokyo MX1
https://movie.mcas.jp/switcher/mcas1_2/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://static.wikia.nocookie.net/logopedia/images/1/1d/20150701201731.png/revision/latest/scale-to-width-down/403?cb=20200512214408" group-title="🏷️ | Kênh JAPAN",Tokyo MX2
https://movie.mcas.jp/mcas/mx2_2/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://global.weathernews.com/wp-content/themes/custom-thema/images/common/logo.svg" group-title="🏷️ | Kênh JAPAN",Weather News
https://movie.mcas.jp/mcas/wn1_2/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://static.epg.best/jp/NipponTV.jp.png" group-title="🏷️ | Kênh JAPAN",Nippon TV (JOAX-DTV)
http://redlabmcdn.s.llnwi.net/jp04/ryowa3hd/playlist.m3u8
#EXTINF:-1 tvg-logo="http://www.arirang.com/images/index/arirang.png" group-title="🏷️ | Kênh SOUTH KOREA",Arirang Korea (아리랑 TV)
https://amdlive-ch01-ctnd-com.akamaized.net/arirang_1ch/smil:arirang_1ch.smil/chunklist_b2256000_sleng.m3u8
#EXTINF:-1 tvg-logo="http://img.imbc.com/commons/2018/image/main/mbc-logo.png" group-title="🏷️ | Kênh SOUTH KOREA",MBC HD 
http://vod.mpmbc.co.kr:1935/live/encoder-tv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://image.tving.com/upload/cms/caic/CAIC1600/C00551.png" group-title="🏷️ | Kênh SOUTH KOREA",tVN HD 
http://gg.gg/tVN720p
#EXTINF:-1 tvg-logo="https://image.tving.com/upload/cms/caic/CAIC1600/C01141.png" group-title="🏷️ | Kênh SOUTH KOREA",tvN SHOW HD 
http://gg.gg/tvNSHOW720p
#EXTINF:-1 tvg-logo="http://www.knn.co.kr/wp-content/themes/knnblog/images/logo.png" group-title="🏷️ | Kênh SOUTH KOREA",KNN - 부산방송
http://211.220.195.200:1935/live/mp4:KnnTV.sdp/playlist.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/MBN_Channel_Logo.svg/640px-MBN_Channel_Logo.svg.png" group-title="🏷️ | Kênh SOUTH KOREA",MBN - 매일방송
http://origin.flive.skcdn.com/mbn-auth1/1000k/playlist.m3u8
#EXTINF:-1 tvg-logo="https://www.ytn.co.kr/img/comm/logo_ytn_w.png" group-title="🏷️ | Kênh SOUTH KOREA",YTN
http://slive.ytn.co.kr/ytn/_definst_/ytn_stream_20190306/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://image.ytn.co.kr/ytn/replay/ch_logo_4.png" group-title="🏷️ | Kênh SOUTH KOREA",YTN dmb
http://slive.ytn.co.kr:1935/dmb/ydlive_20140419_1/chunklist_w1389588282.m3u8
#EXTINF:-1 tvg-logo="https://static.epg.best/kr/YTNScience.kr.png" group-title="🏷️ | Kênh SOUTH KOREA",YTN Science
http://slive.sciencetv.kr:1935/science/yslive_20140419_1/chunklist_w646673757.m3u8
#EXTINF:-1 tvg-logo="https://image.tving.com/upload/cms/caic/CAIC1700/C01101.png" group-title="🏷️ | Kênh SOUTH KOREA",YTN Life
https://slive.ytn.co.kr/weather/weather_20140419_1/chunklist_w556856077.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh CHINA" tvg-logo="https://uphinh.vn/images/2020/07/01/a891c59491dbeda845d37d02b2df1b5c.png",Truyền hình An Huy (安徽卫视)
http://gg.gg/anhuimac
#EXTINF:-1 group-title="🏷️ | Kênh CHINA" tvg-logo="https://static.ivanti.com/sites/marketing/media/images/logos/customers-color/btv_logo-color.png",Truyền hình Bắc Kinh (北京卫视)
http://111.63.117.13:6060/030000001000/G_BEIJING/G_BEIJING.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh CHINA" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/7/7f/DragonTV_logo.png",Truyền hình Thượng Hải (东方卫视)
http://111.63.117.13:6060/030000001000/G_DONGFANG/G_DONGFANG.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh CHINA" tvg-logo="https://upload.wikimedia.org/wikipedia/en/3/3b/Jiangsu_Broadcasting_Corporation_Logo.png",Truyền hình Giang Tô (江苏卫视)
http://gg.gg/jiangsumac
#EXTINF:-1 group-title="🏷️ | Kênh CHINA" tvg-logo="https://upload.wikimedia.org/wikipedia/zh/6/65/HBTV_logo.png",Truyền hình Hồ Bắc (湖北卫视)
http://111.63.117.13:6060/030000001000/G_HUBEI/G_HUBEI.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh CHINA" tvg-logo="https://upload.wikimedia.org/wikipedia/en/6/68/HunanTV_logo.png",Truyền hình Hồ Nam (湖南卫视)
http://111.63.117.13:6060/030000001000/G_HUNAN/G_HUNAN.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh CHINA" tvg-logo="https://www.dishpromotions.com/wp-content/uploads/ZTV-logo.png",Truyền hình Chiết Giang (浙江卫视)
http://111.63.117.13:6060/030000001000/G_ZHEJIANG/G_ZHEJIANG.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://cdn.golfnews.vn/bundles/cmnindex/images/GolfNews_Logo_black.png",Golf New TV HD 
https://884030f97a.vws.vegacdn.vn/live/_definst_/stream_1_a0acb/chunklist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.tennischannel.app/image/original/6580da0c-bfd3-407e-ae12-144790330b17.png",Tennis Channel HD 
https://tennischannel-intl-samsung-uk.amagi.tv/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/sporttv-1.png",SPORT.TV1 HD
https://smart-tv.livedoomovie.com:4431/02_SPORTTV_1_720p/chunklist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/sporttv-2.png",SPORT.TV2 HD
https://smart-tv.livedoomovie.com:4431/02_SPORTTV_2_720p/chunklist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/sporttv-3.png",SPORT.TV3 HD
https://smart-tv.livedoomovie.com:4431/02_SPORTTV_3_720p/chunklist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/sporttv-4.png",SPORT.TV4 HD
https://smart-tv.livedoomovie.com:4431/02_SPORTTV_4_720p/chunklist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/sporttv-5.png",SPORT.TV5 HD
https://smart-tv.livedoomovie.com:4431/02_SPORTTV_5_720p/chunklist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.thesportsdb.com/images/media/logo/RMC_Sport_1.png", RMC SPORT 1 HD
http://185.184.192.166/RMC1/mpegts
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.thesportsdb.com/images/media/logo/RMC_Sport_2.png",RMC SPORT 2 HD
http://185.184.192.166/RMC2/mpegts
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/eleven-sports-1-hd.png",ELEVEN SPORTS 1 HD POL
http://207.110.52.61:8080/s/hls/5/3570/eleven_sports_1_355/1/1/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/eleven-sports-2-hd.png",ELEVEN SPORTS 2 HD POL
http://207.110.52.61:8080/s/hls/5/9335/eleven_sports_2_303/1/1/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.thesportsdb.com/images/media/logo/owa6og1571337802.png", NBATV
http://84.22.33.215/nbatv/mpegts
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS"  tvg-logo="https://www.sanmarinortv.sm/assets/frontend/img/logo-90.png",RTV San Marino Sport HD
http://d2hrvno5bw6tg2.cloudfront.net/smrtv-ch02/_definst_/ch-02/chunklist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS"  tvg-logo="https://vod.sportstv.com.tr/categoryicons/Anasayfa-1622751464-icon.png",Sports TV Turkey
http://live.sportstv.com.tr/hls/low/sportstv_fhd/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS"  tvg-logo="https://www.sport2u.tv/wp-content/uploads/2021/05/logo-sport2u.png",Sport 2U
http://live.sport2u.tv:1935/EvoLive/myStream/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.thesportsdb.com/images/media/channel/logo/k3gmp81628519750.png", Match TV
https://bal.varcdn1.ru/lb/match/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/TringSport1.png",Tring Sport 1 HD
http://93.157.62.180/TringSport1HD/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/TringSport2.png",Tring Sport 2 HD
http://93.157.62.180/TringSport2HD/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.tvshqipon.com/wp-content/uploads/2019/06/Super-Sport-1-Live.png", Super Sport 1 HD
http://93.157.62.180/Supersport1/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.tvshqipon.com/wp-content/uploads/2019/06/Super-Sport-2-Live.png", Super Sport 2 HD
http://93.157.62.180/Supersport2/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.tvshqipon.com/wp-content/uploads/2019/06/SuperSport-3-Live.png", Super Sport 3 HD
http://93.157.62.180/Supersport3/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/kujtesasport1.png", Kujtesa Sport 1 
http://93.157.62.180/KSport1/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/kujtesasport2.png", Kujtesa Sport 2
http://93.157.62.180/KSport2/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/kujtesasport3.png", Kujtesa Sport 3
http://93.157.62.180/KSport3/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/kujtesasport4.png", Kujtesa Sport 4
http://93.157.62.180/KSport4/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://assets.bein.com/mena/sites/3/2015/06/beIN_SPORTS1_PREMIUM_Digital_Mono.png",beIN SPORTS 1 PREMIUM
http://130.193.166.18/cache/Bein-Prem-1-HEVC/master.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://assets.bein.com/mena/sites/3/2015/06/beIN_SPORTS2_PREMIUM_Digital_Mono.png",beIN SPORTS 2 PREMIUM
http://130.193.166.18/cache/Bein-Prem-2-HEVC/master.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://assets.bein.com/mena/sites/3/2015/06/beIN_SPORTS3_PREMIUM_Digital_Mono.png",beIN SPORTS 3 PREMIUM
http://130.193.166.18/cache/Bein-Prem-3-HEVC/master.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="http://www.talhouk.com/tv/Logos/Canal+_Sport_HD.png",CANAL + SPORTS
http://207.110.52.61:8080/s/hls/5/293/canal_plus_sport_polska_250/1/1/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.primaplay.ro/assets/imgs/channel/looksportplus.png",LOOK SPORT + HD
https://stream1.1616.ro:1945/lookplus/livestream/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.primaplay.ro/assets/imgs/channel/looksport.png",LOOK SPORT  HD
https://stream1.1616.ro:1945/look/livestream/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.primaplay.ro/assets/imgs/channel/looksport2.png",LOOK SPORT 2 HD
https://stream1.1616.ro:1945/looksport2/livestream/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.primaplay.ro/assets/imgs/channel/looksport2.png",LOOK SPORT 3 HD
https://stream1.1616.ro:1945/looksport3/livestream/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" logo="https://chungmaster.github.io/logo/RTSHSport.png",RTSH Sport HD
https://tvlive.rtsh.dev/live/sport_ott_p3/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="http://onegolftv.com/wp-content/uploads/2018/08/onegolf-HD-with-image-512.png",ONE GOLF HD
http://162.250.201.58:6211/pk/ONEGOLF/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.realmadrid.com/img/horizontal_940px/logotipo_rmtv_940x400thumb_h_20200128014053.jpg", Real Madrid TV
http://154.62.74.11:1935/live/realmadridnntv/chunklist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://logos-download.com/wp-content/uploads/2016/09/Red_Bull_TV_logo.png",Red Bull TV Original
http://gg.gg/redbulltv_original
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://logos-download.com/wp-content/uploads/2016/09/Red_Bull_TV_logo.png",Red Bull TV HD
https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master_6660.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="http://static.epg.best/gr/EdgeSport.gr.png" , Edge Sports HD 
https://dai.google.com/linear/hls/event/d4zeSI-dTuqizFrByjs3OA/master.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS"  tvg-logo="http://static.epg.best/us/Stadium.us.png" , Stadium
https://stadiumlivein-i.akamaihd.net/hls/live/522512/mux_4/master.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS"  tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/82/CBS_Sports_HQ.png" ,CBS Sports HQ
http://dai.google.com/linear/hls/event/9Lq0ERvoSR-z9AwvFS-xYA/master.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS"  tvg-logo="https://kokfights.com/wp-content/uploads/2018/05/kok_logo.png" ,KOK Fights HD
https://live-k2301-kbp.1plus1.video/sport/smil:sport.smil/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS"  tvg-logo="https://snagfilms-a.akamaihd.net/cf9c3bbc-917a-4447-90ab-55bf78b01f49/images/83/36/d90134124307b18e251dce2033ad/1566507637959_laximages-tab.png" ,LSN - Lax Sports Network
https://1840769862.rsc.cdn77.org/FTF/LSN_SCTE.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS"  tvg-logo="https://chungmaster.github.io/logo/dubairacing.png",DUBAI RACING EVENT UAE
http://dmisvthvll.cdn.mangomolo.com/events/smil:events.smil/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/dubairacing.png",DUBAI RACING UAE
http://dmithrvll.cdn.mangomolo.com/dubairacing/smil:dubairacing.smil/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/dubairacing3.png",DUBAI RACING 3 UAE
http://dmithrvll.cdn.mangomolo.com/dubaimubasher/smil:dubaimubasher.smil/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="http://static.epg.best/au/RacingCom.au.png" , Racing.com
https://racingvic-i.akamaized.net/hls/live/598695/racingvic/1500.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://media.info/i/lf/300/1514269404/6402.png" ,Sky Racing 1
https://skylivesky-i.akamaihd.net/hls/live/569780/skylive/sky1_extreme@569780.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://media.info/i/lf/300/1514269377/6411.png" ,Sky Racing 2
https://skylivesky-i.akamaihd.net/hls/live/569780/skylive/sky2_extreme@569780.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://i.imgur.com/XakLUm4.png" ,Australian  Sports Channel
https://austchannel-live.akamaized.net/hls/live/2002736/austchannel-sport/master.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://chungmaster.github.io/logo/skyracingcentral.png" ,Sky Thoroughbred Central
https://skylivesky-i.akamaihd.net/hls/live/569780/skylive/stcsd_extreme@569780.m3u8
EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/FITE_TV.svg/1200px-FITE_TV.svg.png" ,FITE 24/7 HD
https://cdn-cf.fite.tv/linear/fite247/playlist.m3u8
EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://mmajunkie.usatoday.com/wp-content/uploads/sites/91/2017/07/mmaj-header-logo.png",MMA Junkie HD
https://a.jsrdn.com/broadcast/80f6ba72c8/+0000/high/c.m3u8
EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.flosports.tv/wp-content/uploads/2020/05/FloSports-Secondary-igniteblack.png",MMA TV
https://a.jsrdn.com/broadcast/47cff5378f/+0000/high/c.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/MLS_crest_logo_RGB_gradient.svg/1200px-MLS_crest_logo_RGB_gradient.svg.png" , MLS Soccer TV
https://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5cb626cfcaf83414128f439c/master.m3u8?deviceType=web&deviceMake=Chrome&deviceModel=Chrome&sid=d1634607-2892-447a-b316-17a106f905fb&deviceId=9f228953-21cb-4b82-a393-dd32d047379f&deviceVersion=76.0.3809.132&appVersion=2.7.4-9a7fc53e0c1da468e3c566c3f53e98a36ca1f97b&deviceDNT=0&userId=&advertisingId=&deviceLat=45.4994&deviceLon=-73.5703&app_name=&appName=web&buildVersion=&appStoreUrl=&architecture=&serverSideAds=true
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://i.ibb.co/4jGtHGt/EXTV-BEARTV.png", Extreme Sports HD 
http://58.65.171.202:8000/play/10506/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://i.imgur.com/LS2PSpt.png",EUROSPORT 1
http://154.62.74.12:1935/live/smil:eurosport1nntv.smil/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://i.imgur.com/TxipcCK.png",EUROSPORT 2
http://154.62.74.12:1935/live/smil:eurosport2hdnntv.smil/playlist.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://www.cableman.ru/sites/default/files/eurosport_gold.png",EUROSPORT GOLD
http://185.228.135.48:8080/tv_eurosport_gold_hd/index.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://i.imgur.com/R3q0EEE.png",FANDUEL SPORTS GRID
https://dai2.xumo.com/amagi_hls_data_xumo1212A-xumosportsgrid/CDN/master.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/DAZN_1_Logo.svg/2560px-DAZN_1_Logo.svg.png", DAZN 1
http://xfire.one:88/live/test1/test2/22878.m3u8
#EXTINF:-1 group-title="🏷️ | Kênh SPORTS" tvg-logo="https://static.wikia.nocookie.net/logopedia/images/a/ac/DAZN2_2021.png/revision/latest?cb=20210308203636", DAZN 2
http://xfire.one:88/live/test1/test2/22879.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://media.vov.vn/sites/default/files/2020-12/vov1_2.png", VOV1
https://str.vov.gov.vn/vovlive/vov1vov5Vietnamese.sdp_aac/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://media.vov.vn/sites/default/files/2020-12/vov2_2.png", VOV2
https://str.vov.gov.vn/vovlive/vov2.sdp_aac/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://media.vov.vn/sites/default/files/2020-12/vov3_2.png", VOV3
https://str.vov.gov.vn/vovlive/vov3.sdp_aac/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://media.vov.vn/sites/default/files/2020-12/vov4_2.png", VOV4 ĐBSCL
http://media.kythuatvov.vn:1936/live/VOV4_CT.sdp/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Logo_VOV.svg/1280px-Logo_VOV.svg.png", VOV 24/7 
http://media.kythuatvov.vn:7007/;stream/
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://media.vov.vn/sites/default/files/2020-12/vov5new_0.png", VOV5
http://media.kythuatvov.vn:1936/live/VOV5.sdp/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://vovgiaothong.vn/Data/Sites/1/logos/VOVGT_1.png", VOV Giao thông Hà Nội
http://media.kythuatvov.vn:1936/live/VOVGTHN.sdp/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://vovgiaothong.vn/Data/Sites/1/logos/VOVGT_1.png", VOV Giao thông Hồ Chí Minh
http://media.kythuatvov.vn:1936/live/VOVGTHCM.sdp/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://kythuatvov.vn/wp-content/uploads/2021/01/Logo-50.png", VOV Mekong
http://media.kythuatvov.vn:1936/live/MEKONG.sdp/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://kythuatvov.vn/wp-content/uploads/2021/01/Logo-51.png", VOV Sức khỏe 89
http://media.kythuatvov.vn:1936/live/VOV89.sdp/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://voh.com.vn/images/icons/icon-small-1.png", VOH FM 99.9Mhz
https://strm.voh.com.vn/radio/channel3/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://voh.com.vn/images/icons/icon-small-4.png", VOH FM 95.6Mhz
https://strm.voh.com.vn/radio/channel1/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://voh.com.vn/images/icons/icon-small-3.png", VOH FM 87.7Mhz
https://strm.voh.com.vn/radio/channel5/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://voh.com.vn/images/icons/icon-small-2.png", VOH AM 610Khz
https://strm.voh.com.vn/radio/channel2/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/8a/Xone-logo.jpg", Xone FM
https://zle-mplaylist.zadn.vn/_wNzFrRgLM8/zhls/live/71b510722c37c5699c26/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://theoneradio.vn/Content/images/logo.png", The One Radio
https://vnno-pt-3-tf-playlist-live-zmp3.zadn.vn/C0ti9DKXaS4/zhls/live/standard-audio/5c0872cf4e8aa7d4fe9b/standard-audio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://media.hanoitv.vn/upload/logo_joy.png", Joy FM
http://cdn.mediatech.vn/hntvRadio/joyfm.stream_aac/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://img.hplus.com.vn/728x409/banner/2018/06/06/101889-BaRia.png", Bà Rịa Vũng Tàu
http://113.163.216.23:1935/live/radio1.sdp_audio/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://thbl.vn/radio.png", Bạc Liêu
https://tv.thbl.vn/live/radio/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://tvonline.vn/wp-content/uploads/2018/07/large_tbk.jpg", Bắc Kạn
http://113.160.162.131:8080/hls/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://bacgiangtv.vn/templates/frontend/bgtv/Assets/img/logo.png", Bắc Giang
http://cdn.mediatech.vn/bgtvlive/radiolive/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://tvonline.vn/wp-content/uploads/2018/07/large_bacninh.png", Bắc Ninh
http://118.107.85.4:1935/radio/bacninh_aac/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://thbt.vn/wp-content/themes/comfy-plus/styles/default/img/tv.png", Bến Tre
http://113.163.94.245/hls-live/livepkgr/_definst_/liveevent/audiostream.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://img.btv.org.vn:81/upload/vod/10112016/1478747759_kenhbtvRadiogif.gif", Bình Dương
https://btvfm011220.cdn.vnns.io/btv-fm.tms/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://media.baobinhphuoc.com.vn/upload/files/logo/bpradio.png", Bình Phước
https://live.baobinhphuoc.com.vn/bptvlive/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://binhthuantv.vn/wp-content/themes/dongthap//favicon.png", Bình Thuận
http://202.43.109.142:1935/thbtradio/btradio/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://118.69.199.136/wp-content/uploads/2014/01/radio_online.jpg", Cà Mau
http://tv.ctvcamau.vn/live/radio/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://canthotv.vn/wp-content/uploads/2018/02/973FM.jpg", Cần Thơ
https://mekongpassion.com/live/radio/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://danangtv.vn/images/radio.png", Đà Nẵng
http://drtdnglive.e49a7c38.cdnviet.com/liveradio/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://upload.wikimedia.org/wikipedia/vi/c/c5/%C4%90N-RTV.png", Đồng Nai
http://118.107.85.5:1935/radio/dongnai_aac/playlist.m3u8 
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://www.thdt.vn/wp-content/uploads/2018/11/logo2-1.png", Đồng Tháp
http://202.43.109.144:1935/thdtradio/thdtradio/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://gialaitv.vn/wp-content/uploads/2017/02/audio2-1.gif", Gia Lai
http://113.161.25.3:8134/hls/radio/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://hagiangtv.vn/common/v1/images/0000889050_a.jpeg", Hà Giang
http://113.162.84.113:8081/
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://hanamtv.vn/upload/info/hanam_poster.jpg", Hà Nam
http://103.90.220.236/thhnlive/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://scloud3.mediatech.vn/upload/6/channel/mediatech.1561362623.5d1080bf05230.png", Hà Nội FM 90
http://cdn.mediatech.vn/hntvRadio/fm90.sdp_aac/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://scloud3.mediatech.vn/upload/6/channel/mediatech.1561362644.5d1080d463d70.png", Hà Nội FM 96
http://cdn.mediatech.vn/hntvRadio/fm96.sdp_aac/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://hatinhtv.vn/img/live-poster.jpg", Hà Tĩnh
http://hatinhtv.vn/phatthanh/m3u8/audio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://www.haiduongtv.com.vn/upload/news/icon//20.2018/1526269157_NENPHATTHANH.jpg", Hải Dương
http://113.160.131.11:8000/
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://thhp.vn/common/v1/images/radio1.png", Hải Phòng FM 93.7Mhz
https://live.thhp.vn/937/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://thhp.vn/common/v1/images/radio2.png", Hải Phòng FM 102.2Mhz
https://live.thhp.vn/radio/102/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://haugiangtivi.vn/public/Home/imghg/logohg.png", Hậu Giang
https://haugiangfm011220.cdn.vnns.io/haugiang-fm.tms/chunks.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://hungyentv.vn//templates/frontend/hytv/Assets/img/backgroud-radio.jpg", Hưng Yên
http://103.90.220.236/hytvlive/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://ktv.org.vn/wp-content/themes/ktv/assets/img/logo.png", Khánh Hòa
http://210.245.20.94/hls/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://kgtv.vn/wp-content/uploads/2015/07/radio.png", Kiên Giang
http://tv.kgtv.vn/live/kgaudio/kgaudio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://kontumtv.vn/wp-content/uploads/2020/12/FM95.1-1.jpg", Kon Tum
https://tv.kontumtv.vn/live/radio/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://lamdongtv.vn/images/thumbs/0000885408_a.jpeg", Lâm Đồng
http://118.107.85.4:1935/radio/lamdong_aac/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://la34.com.vn/wp-content/themes/carrington-mobile/img/logo.png", Long An
http://113.161.229.13/hls-live/livepkgr/_definst_/liveevent/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://langsontv.vn/templates/frontend/lstv/Assets/img/radio_bg.png", Lạng Sơn
https://stream.zeno.fm/xsct365wra0uv
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://laichautv.vn/dataimages/201512/original/images1225848_logo1.png", Lai Châu
https://ll4mfr7mnaliv.vcdn.cloud/laichau/radio/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://truyenhinhnghean.vn/common/v1/image/logo_fb.jpg", Nghệ An
https://live.truyenhinhnghean.vn/hls/na2/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://nbtv.vn/templates/frontend/nbtv/Assets/img/audio_bg.jpg", Ninh Bình
https://103.90.220.236/nbtvlive/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://ptpphuyen.vn/dataimages/202012/original/images2981323_banner_ptp_tet_2021.gif", Phú Yên
http://113.161.4.48:8080/phuyen/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://qrt.vn/wp-content/themes/qtitv-child/images/bg-phat-thanh.png", Quảng Nam
http://113.161.6.157:8085/phatthanh/QRT.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://quangngaitv.vn/Images/Favicon/favicon.ico", Quảng Ngãi
http://118.107.85.5:1935/radio/quangngai_aac/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://media.baoquangninh.com.vn/upload/files/logo/logotrangchu4.png", QNR1 - Quảng Ninh
http://103.90.220.236/qtvlive/qnr1.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://media.baoquangninh.com.vn/upload/files/logo/logotrangchu3.png", QNR2 - Quảng Ninh
http://103.90.220.236/qtvlive/qnr2.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://quangtritv.vn/images/no_pic.png", Quảng Trị
http://103.90.220.236/qrtvlive/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://thst.vn/Content/images/fm.png", Sóc Trăng
http://115.78.3.164:8135/liveeventf.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://truyenhinhso.vn/wp-content/uploads/2020/06/son-la.png", Sơn La
http://118.107.85.5:1935/radio/sonla_aac/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://trt.ohi.vn/frontend/home/images/bg_radio.jpg", Thừa Thiên Huế
http://trtlive.f77de468.cdnviet.com/Radio-online/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://esb.thainguyentv.vn/upload/group/news//hytvgo_5ff2dd1ed1b81.jpg", Thái Nguyên
http://media.mediatech.vn:1935/tntvlive/tnra/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://ttv11.vn/public/Home/images/logotayninh.png", Tây Ninh
http://202.43.109.142:1935/radio11/tnradio/chunklist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://thaibinhtv.vn/templates/frontend/tbtv/Assets/img/logo.png", Thái Bình
http://118.70.118.191:1935/tbtvlive/radio/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="http://www.thtg.vn/wp-content/themes/thtg-mobile/img/radio.png", Tiền Giang
http://thtg.vn:8002/radiolive.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://tuyenquangtv.vn/file/fb9e3a036ab59c2c016ac3618a0d3aec/fb9e3a036ab59c2c016b2c08c1835d52/062019/TTVchantrang_20190620104114.png", Tuyên Quang
https://live.tuyenquangtv.vn/hls/radio.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/6/62/Logo_THVL_RADIO.png", Vĩnh Long
https://thvli-live2.admon.com.vn/thvli/thvlradio/playlist.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://yenbaitv.org.vn/modules/frontend/themes/ptthyb/images/logo-footer-small.png", Yên Bái
http://bk.yenbaitv.org.vn/hls/audio/livestream.m3u8 
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgICQ2ciKiAoMCxIOU3RhdGlvblByb2ZpbGUYgICQucnHqwsMogEEemVubw/image/", M Radio Việt Nam
https://stream.zeno.fm/4q7y9hvkp2zuv
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgICQ2ciKiAoMCxIOU3RhdGlvblByb2ZpbGUYgIDQoL-YpAoMogEEemVubw/image/", Cải Lương Việt Nam
https://stream.zeno.fm/0trm6wrnga0uv
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgICQ2ciKiAoMCxIOU3RhdGlvblByb2ZpbGUYgICQ7brTsQgMogEEemVubw/image/", Radio Nhạc Vàng Xưa
https://stream.zeno.fm/x2z45v7d84zuv
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgICQ2ciKiAoMCxIOU3RhdGlvblByb2ZpbGUYgIDQidjS_wkMogEEemVubw/image/", Radio DJ
https://stream.zeno.fm/ehbutdfccm0uv
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgICQ2ciKiAoMCxIOU3RhdGlvblByb2ZpbGUYgIDQiavcsgsMogEEemVubw/image/", Radio Phật Giáo
https://stream.zeno.fm/8456uy0bcm0uv
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgICQ2ciKiAoMCxIOU3RhdGlvblByb2ZpbGUYgICw0ILTsQoMogEEemVubw/image/", Radio Nhạc Dân Ca
https://stream.zeno.fm/a2dbs2tq1p8uv
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgIDg2_XVmgsMCxIOU3RhdGlvblByb2ZpbGUYgIDQi9zzhAgMogEEemVubw/image/", Radio Nhạc Xuân
https://stream.zeno.fm/hvtxgd85rm0uv
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgIDQz-yvmQsMCxIOU3RhdGlvblByb2ZpbGUYgIDQ7-DDtAgMogEEemVubw/image/", Âm Nhạc Không Khoảng Cách
https://stream.zeno.fm/bnuzk0znhm8uv
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://proxy.zeno.fm/content/stations/agxzfnplbm8tc3RhdHNyMgsSCkF1dGhDbGllbnQYgIDg2_XVmgsMCxIOU3RhdGlvblByb2ZpbGUYgIDQ6_SHwgoMogEEemVubw/image/", Những Bản Acoustic Cover Hay Nhất
https://stream.zeno.fm/tk8atfbgtg8uv
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://cherryradio.com.au/images/kenhtintuc-player.png", Cherry Radio Tin Tức
https://sslstreaming.com:7017/;
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://cherryradio.com.au/images/nhactritinh-player.png", Cherry Radio Trữ Tình
https://stream.zeno.fm/wppep1n7qpeuv.aac 
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://cherryradio.com.au/images/nhactritinh-player.png", Cherry Radio Nhạc Trẻ
https://stream.zeno.fm/umt5gqmg3reuv.aac
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/8/5/4/0/854010f76bddeefd5f13305a1d6cc8be.jpg", Zing MP3 - On Air
https://multi-playlist-zmp3.zadn.vn/9tPzLPYORS8/zhls/playback-realtime/a07d79b945fcaca2f5ed/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/7/7/8/d/778d152062edfbe0e4c4abf151858bf0.jpg", Zing MP3 - Chạm
https://multi-playlist-zmp3.zadn.vn/62YE6lXdY4w/zhls/playback-realtime/db68d4afe8ea01b458fb/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/1/4/6/b/146b49d11cc9b3bc591823bfedb8bce2.jpg", Zing MP3 - Vpop
https://multi-playlist-zmp3.zadn.vn/wTSwRIGOON0/zhls/playback-realtime/6eeb692c5569bc37e578/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/0/9/9/3/0993b3110c60ba6518fceeba9913d20d.jpg", Zing MP3 - Acoustic
https://multi-playlist-zmp3.zadn.vn/ktkT8IgzcQQ/zhls/playback-realtime/08aae96dd5283c766539/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/1/3/0/5/1305cd954d22d89fef4354301613fd68.jpg", Zing MP3 - Bolero
https://multi-playlist-zmp3.zadn.vn/BtRvAOtW5jk/zhls/playback-realtime/e3b9f87ec43b2d65742a/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/b/f/3/b/bf3bf87a788a5d0b8719c6feee774a2e.jpg", Zing MP3 - Rap Việt
https://multi-playlist-zmp3.zadn.vn/Itsn5VCb5Uo/zhls/playback-realtime/4f2980eebcab55f50cba/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/c/f/2/4/cf2428f7e56a8c2a52d84cb106891de2.jpg", Zing MP3 - Kpop
https://multi-playlist-zmp3.zadn.vn/94rxZ-Dfzro/zhls/playback-realtime/ff294ded71a898f6c1b9/index.m3u8
#EXTINF:-1 group-title="📻 | Radio" tvg-logo="https://photo-zmp3.zadn.vn/avatars/b/0/d/a/b0da7c8ecd6521337682f3a86fa0170f.jpg", Zing MP3 - USUK
https://multi-playlist-zmp3.zadn.vn/RckDo1XPsU4/zhls/playback-realtime/111c87d8bb9d52c30b8c/index.m3u8

'''
import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/chungplay/chungplay.github.io/main/assets/chung_na.m3u')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/chungplay/chungplay.github.io/main/assets/chung_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U url-tvg="http://onetv.click/schedule/epg.xml" tvg-shift=0 cache=500 deinterlace=1 aspect-ratio=16:9 m3uautoload=1')
print(banner)
s = requests.Session()
with open('../URL_link.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
