; ModuleID = ""
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i64 @"__arybo"(i64 %"SymVar_0") nounwind
{
.3:
  %".4" = zext i8 3 to i64
  %".5" = and i64 %".4", 63
  %".6" = lshr i64 %"SymVar_0", %".5"
  %".7" = zext i8 61 to i64
  %".8" = and i64 %".7", 63
  %".9" = shl i64 %"SymVar_0", %".8"
  %".10" = or i64 %".6", %".9"
  %".11" = sub i64 %".10", 1072693119
  %".12" = or i64 %"SymVar_0", %".11"
  %".13" = sub i64 %".12", 300260246
  %".14" = lshr i64 %".13", 32
  %".15" = trunc i64 %".14" to i8
  %".16" = zext i8 %".15" to i32
  %".17" = lshr i64 %".13", 40
  %".18" = trunc i64 %".17" to i8
  %".19" = zext i8 %".18" to i32
  %".20" = shl i32 %".19", 8
  %".21" = or i32 %".16", %".20"
  %".22" = lshr i64 %".13", 48
  %".23" = trunc i64 %".22" to i8
  %".24" = zext i8 %".23" to i32
  %".25" = shl i32 %".24", 16
  %".26" = or i32 %".21", %".25"
  %".27" = lshr i64 %".13", 56
  %".28" = trunc i64 %".27" to i8
  %".29" = zext i8 %".28" to i32
  %".30" = shl i32 %".29", 24
  %".31" = or i32 %".26", %".30"
  %".32" = zext i32 %".31" to i64
  %".33" = trunc i64 %".32" to i32
  %".34" = zext i32 %".33" to i64
  %".35" = trunc i64 %".34" to i32
  %".36" = zext i32 %".35" to i64
  %".37" = trunc i64 %".36" to i32
  %".38" = zext i32 %".37" to i64
  %".39" = trunc i64 %".38" to i32
  %".40" = trunc i32 %".39" to i8
  %".41" = zext i8 %".40" to i64
  %".42" = trunc i64 %".38" to i32
  %".43" = lshr i32 %".42", 8
  %".44" = trunc i32 %".43" to i8
  %".45" = zext i8 %".44" to i64
  %".46" = shl i64 %".45", 8
  %".47" = or i64 %".41", %".46"
  %".48" = trunc i64 %".38" to i32
  %".49" = lshr i32 %".48", 16
  %".50" = trunc i32 %".49" to i8
  %".51" = zext i8 %".50" to i64
  %".52" = shl i64 %".51", 16
  %".53" = or i64 %".47", %".52"
  %".54" = trunc i64 %".38" to i32
  %".55" = lshr i32 %".54", 24
  %".56" = trunc i32 %".55" to i8
  %".57" = zext i8 %".56" to i64
  %".58" = shl i64 %".57", 24
  %".59" = or i64 %".53", %".58"
  %".60" = trunc i64 %".13" to i8
  %".61" = zext i8 %".60" to i32
  %".62" = lshr i64 %".13", 8
  %".63" = trunc i64 %".62" to i8
  %".64" = zext i8 %".63" to i32
  %".65" = shl i32 %".64", 8
  %".66" = or i32 %".61", %".65"
  %".67" = lshr i64 %".13", 16
  %".68" = trunc i64 %".67" to i8
  %".69" = zext i8 %".68" to i32
  %".70" = shl i32 %".69", 16
  %".71" = or i32 %".66", %".70"
  %".72" = lshr i64 %".13", 24
  %".73" = trunc i64 %".72" to i8
  %".74" = zext i8 %".73" to i32
  %".75" = shl i32 %".74", 24
  %".76" = or i32 %".71", %".75"
  %".77" = zext i32 %".76" to i64
  %".78" = trunc i64 %".77" to i32
  %".79" = zext i32 %".78" to i64
  %".80" = trunc i64 %".79" to i32
  %".81" = trunc i32 %".80" to i8
  %".82" = zext i8 %".81" to i64
  %".83" = shl i64 %".82", 32
  %".84" = or i64 %".59", %".83"
  %".85" = trunc i64 %".79" to i32
  %".86" = lshr i32 %".85", 8
  %".87" = trunc i32 %".86" to i8
  %".88" = zext i8 %".87" to i64
  %".89" = shl i64 %".88", 40
  %".90" = or i64 %".84", %".89"
  %".91" = trunc i64 %".79" to i32
  %".92" = lshr i32 %".91", 16
  %".93" = trunc i32 %".92" to i8
  %".94" = zext i8 %".93" to i64
  %".95" = shl i64 %".94", 48
  %".96" = or i64 %".90", %".95"
  %".97" = trunc i64 %".79" to i32
  %".98" = lshr i32 %".97", 24
  %".99" = trunc i32 %".98" to i8
  %".100" = zext i8 %".99" to i64
  %".101" = shl i64 %".100", 56
  %".102" = or i64 %".96", %".101"
  %".103" = sext i64 %"SymVar_0" to i128
  %".104" = sext i64 %".11" to i128
  %".105" = mul i128 %".103", %".104"
  %".106" = trunc i128 %".105" to i64
  %".107" = sext i64 %".106" to i128
  %".108" = zext i8 7 to i64
  %".109" = and i64 %".108", 63
  %".110" = shl i64 %".13", %".109"
  %".111" = sext i64 %".110" to i128
  %".112" = mul i128 %".107", %".111"
  %".113" = trunc i128 %".112" to i64
  %".114" = sub i64 %"SymVar_0", 2305843009341932414
  %".115" = add i64 %".113", %".114"
  %".116" = and i64 %".115", 63
  %".117" = zext i8 4 to i64
  %".118" = and i64 %".117", 63
  %".119" = shl i64 %".116", %".118"
  %".120" = or i64 %".102", %".119"
  %".121" = trunc i64 %".120" to i8
  %".122" = zext i8 %".121" to i64
  %".123" = lshr i64 %".120", 40
  %".124" = trunc i64 %".123" to i8
  %".125" = zext i8 %".124" to i32
  %".126" = zext i32 %".125" to i64
  %".127" = trunc i64 %".126" to i8
  %".128" = zext i8 %".127" to i32
  %".129" = zext i32 %".128" to i64
  %".130" = trunc i64 %".129" to i8
  %".131" = zext i8 %".130" to i32
  %".132" = zext i32 %".131" to i64
  %".133" = trunc i64 %".132" to i8
  %".134" = zext i8 %".133" to i32
  %".135" = zext i32 %".134" to i64
  %".136" = trunc i64 %".135" to i8
  %".137" = zext i8 %".136" to i32
  %".138" = zext i32 %".137" to i64
  %".139" = trunc i64 %".138" to i8
  %".140" = zext i8 %".139" to i64
  %".141" = shl i64 %".140", 8
  %".142" = or i64 %".122", %".141"
  %".143" = lshr i64 %".120", 16
  %".144" = trunc i64 %".143" to i8
  %".145" = zext i8 %".144" to i64
  %".146" = shl i64 %".145", 16
  %".147" = or i64 %".142", %".146"
  %".148" = lshr i64 %".120", 24
  %".149" = trunc i64 %".148" to i8
  %".150" = zext i8 %".149" to i64
  %".151" = shl i64 %".150", 24
  %".152" = or i64 %".147", %".151"
  %".153" = lshr i64 %".120", 32
  %".154" = trunc i64 %".153" to i8
  %".155" = zext i8 %".154" to i64
  %".156" = shl i64 %".155", 32
  %".157" = or i64 %".152", %".156"
  %".158" = lshr i64 %".120", 8
  %".159" = trunc i64 %".158" to i8
  %".160" = zext i8 %".159" to i32
  %".161" = zext i32 %".160" to i64
  %".162" = trunc i64 %".161" to i8
  %".163" = zext i8 %".162" to i32
  %".164" = zext i32 %".163" to i64
  %".165" = trunc i64 %".164" to i8
  %".166" = zext i8 %".165" to i32
  %".167" = zext i32 %".166" to i64
  %".168" = trunc i64 %".167" to i8
  %".169" = zext i8 %".168" to i64
  %".170" = shl i64 %".169", 40
  %".171" = or i64 %".157", %".170"
  %".172" = lshr i64 %".120", 48
  %".173" = trunc i64 %".172" to i8
  %".174" = zext i8 %".173" to i64
  %".175" = shl i64 %".174", 48
  %".176" = or i64 %".171", %".175"
  %".177" = lshr i64 %".120", 56
  %".178" = trunc i64 %".177" to i8
  %".179" = zext i8 %".178" to i64
  %".180" = shl i64 %".179", 56
  %".181" = or i64 %".176", %".180"
  %".182" = lshr i64 %".11", 32
  %".183" = trunc i64 %".182" to i8
  %".184" = zext i8 %".183" to i32
  %".185" = lshr i64 %".11", 40
  %".186" = trunc i64 %".185" to i8
  %".187" = zext i8 %".186" to i32
  %".188" = shl i32 %".187", 8
  %".189" = or i32 %".184", %".188"
  %".190" = lshr i64 %".11", 48
  %".191" = trunc i64 %".190" to i8
  %".192" = zext i8 %".191" to i32
  %".193" = shl i32 %".192", 16
  %".194" = or i32 %".189", %".193"
  %".195" = lshr i64 %".11", 56
  %".196" = trunc i64 %".195" to i8
  %".197" = zext i8 %".196" to i32
  %".198" = shl i32 %".197", 24
  %".199" = or i32 %".194", %".198"
  %".200" = zext i32 %".199" to i64
  %".201" = trunc i64 %".200" to i32
  %".202" = zext i32 %".201" to i64
  %".203" = trunc i64 %".202" to i32
  %".204" = zext i32 %".203" to i64
  %".205" = trunc i64 %".204" to i32
  %".206" = zext i32 %".205" to i64
  %".207" = trunc i64 %".206" to i32
  %".208" = trunc i32 %".207" to i8
  %".209" = zext i8 %".208" to i64
  %".210" = trunc i64 %".206" to i32
  %".211" = lshr i32 %".210", 8
  %".212" = trunc i32 %".211" to i8
  %".213" = zext i8 %".212" to i64
  %".214" = shl i64 %".213", 8
  %".215" = or i64 %".209", %".214"
  %".216" = trunc i64 %".206" to i32
  %".217" = lshr i32 %".216", 16
  %".218" = trunc i32 %".217" to i8
  %".219" = zext i8 %".218" to i64
  %".220" = shl i64 %".219", 16
  %".221" = or i64 %".215", %".220"
  %".222" = trunc i64 %".206" to i32
  %".223" = lshr i32 %".222", 24
  %".224" = trunc i32 %".223" to i8
  %".225" = zext i8 %".224" to i64
  %".226" = shl i64 %".225", 24
  %".227" = or i64 %".221", %".226"
  %".228" = trunc i64 %".11" to i8
  %".229" = zext i8 %".228" to i32
  %".230" = lshr i64 %".11", 8
  %".231" = trunc i64 %".230" to i8
  %".232" = zext i8 %".231" to i32
  %".233" = shl i32 %".232", 8
  %".234" = or i32 %".229", %".233"
  %".235" = lshr i64 %".11", 16
  %".236" = trunc i64 %".235" to i8
  %".237" = zext i8 %".236" to i32
  %".238" = shl i32 %".237", 16
  %".239" = or i32 %".234", %".238"
  %".240" = lshr i64 %".11", 24
  %".241" = trunc i64 %".240" to i8
  %".242" = zext i8 %".241" to i32
  %".243" = shl i32 %".242", 24
  %".244" = or i32 %".239", %".243"
  %".245" = zext i32 %".244" to i64
  %".246" = trunc i64 %".245" to i32
  %".247" = zext i32 %".246" to i64
  %".248" = trunc i64 %".247" to i32
  %".249" = trunc i32 %".248" to i8
  %".250" = zext i8 %".249" to i64
  %".251" = shl i64 %".250", 32
  %".252" = or i64 %".227", %".251"
  %".253" = trunc i64 %".247" to i32
  %".254" = lshr i32 %".253", 8
  %".255" = trunc i32 %".254" to i8
  %".256" = zext i8 %".255" to i64
  %".257" = shl i64 %".256", 40
  %".258" = or i64 %".252", %".257"
  %".259" = trunc i64 %".247" to i32
  %".260" = lshr i32 %".259", 16
  %".261" = trunc i32 %".260" to i8
  %".262" = zext i8 %".261" to i64
  %".263" = shl i64 %".262", 48
  %".264" = or i64 %".258", %".263"
  %".265" = trunc i64 %".247" to i32
  %".266" = lshr i32 %".265", 24
  %".267" = trunc i32 %".266" to i8
  %".268" = zext i8 %".267" to i64
  %".269" = shl i64 %".268", 56
  %".270" = or i64 %".264", %".269"
  %".271" = add i64 %".113", %".113"
  %".272" = and i64 %".271", 63
  %".273" = zext i8 4 to i64
  %".274" = and i64 %".273", 63
  %".275" = shl i64 %".272", %".274"
  %".276" = or i64 %".270", %".275"
  %".277" = add i64 %".181", %".276"
  %".278" = and i64 %".113", %".114"
  %".279" = and i64 %".278", 15
  %".280" = or i64 %".279", 1
  %".281" = trunc i64 %".280" to i32
  %".282" = zext i32 %".281" to i64
  %".283" = trunc i64 %".282" to i8
  %".284" = zext i8 %".283" to i64
  %".285" = and i64 %".284", 63
  %".286" = shl i64 %".277", %".285"
  %".287" = zext i8 %".121" to i64
  %".288" = zext i8 %".139" to i64
  %".289" = shl i64 %".288", 8
  %".290" = or i64 %".287", %".289"
  %".291" = zext i8 %".144" to i64
  %".292" = shl i64 %".291", 16
  %".293" = or i64 %".290", %".292"
  %".294" = zext i8 %".149" to i64
  %".295" = shl i64 %".294", 24
  %".296" = or i64 %".293", %".295"
  %".297" = zext i8 %".154" to i64
  %".298" = shl i64 %".297", 32
  %".299" = or i64 %".296", %".298"
  %".300" = zext i8 %".168" to i64
  %".301" = shl i64 %".300", 40
  %".302" = or i64 %".299", %".301"
  %".303" = zext i8 %".173" to i64
  %".304" = shl i64 %".303", 48
  %".305" = or i64 %".302", %".304"
  %".306" = zext i8 %".178" to i64
  %".307" = shl i64 %".306", 56
  %".308" = or i64 %".305", %".307"
  %".309" = add i64 %".308", %".276"
  %".310" = and i64 %".113", %".114"
  %".311" = and i64 %".310", 15
  %".312" = or i64 %".311", 1
  %".313" = sub i64 64, %".312"
  %".314" = trunc i64 %".313" to i32
  %".315" = zext i32 %".314" to i64
  %".316" = trunc i64 %".315" to i8
  %".317" = zext i8 %".316" to i64
  %".318" = and i64 %".317", 63
  %".319" = lshr i64 %".309", %".318"
  %".320" = or i64 %".286", %".319"
  ret i64 %".320"
}